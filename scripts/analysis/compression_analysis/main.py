#!/usr/bin/env python3

import os
import sys
import json
import re
from collections import Counter, defaultdict
from copy import deepcopy

# NOTE: this is needed when running on remote server through ssh
# see: https://stackoverflow.com/questions/4706451/how-to-save-a-figure-remotely-with-pylab
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

WBS_DIR = "/scratch/bogdan/tableau-public-bench/data/PublicBIbenchmark-test"
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
BENCHMARK_SRC_DIR = os.path.join(SCRIPT_DIR, "../../../benchmark")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")

FONT_SIZE_BAR = 19
FONT_SIZE_PIE = 14
DEFAULT_COLORS = deepcopy(plt.rcParams['axes.prop_cycle'].by_key()['color'])
DEFAULT_COLORS.extend(["darkgreen", "midnightblue", "black"])
print("nb default colors:", len(DEFAULT_COLORS))
OUT_FILE_FORMAT = "pdf"


def get_datatype_name(sql_datatype):
	return re.split('\(| ', sql_datatype)[0]


class AnalysisManager(object):
	def __init__(self):
		self.table_count = 0
		self.workbooks = defaultdict(lambda: {
			"tables": dict()
		})
		self.datatypes = defaultdict(Counter)
		self.columns = Counter()

	def feed_table(self, wb, table, evaluation_file):
		self.table_count += 1
		compression_method_counter = Counter()

		with open(evaluation_file, 'r') as f:
			stats = json.load(f)
		columns = stats["columns"]

		self.columns[table] = len(columns.keys())

		for col_id, col_data in columns.items():
			data_file = col_data["data_files"]["data_file"]
			datatype_name = get_datatype_name(col_data["col_data"]["datatype"])
			compression_method = data_file["compression"]
			compression_method_counter[compression_method] += 1
			self.datatypes[datatype_name][compression_method] += 1

		self.workbooks[wb]["tables"][table] = compression_method_counter

	def get_stats(self):
		total = sum([t_data for wb, wb_data in self.workbooks.items() for t, t_data in wb_data["tables"].items()], Counter())
		table_average = deepcopy(total)
		for compression_method, count in table_average.items():
			table_average[compression_method] = count / self.table_count

		return {
			"workbooks": self.workbooks,
			"datatypes": self.datatypes,
			"columns": self.columns,
			"table_count": self.table_count,
			"compression_methods":{
				"total": total,
				"table_average": table_average
			}
		}


def output_stats(stats, output_dir):
	out_file = os.path.join(output_dir, "stats.json")
	with open(out_file, 'w') as fp:
		json.dump(stats, fp, indent=2)

	print("[stats] compression_methods={}, datatypes={}".format(json.dumps(stats["compression_methods"], indent=2), json.dumps(stats["datatypes"], indent=2)))


def plot_piechart(values, labels,
			  	  out_file, out_file_format,
			  	  colors=None,
			  	  title=None,
			  	  startangle=None):
	plt.rcParams.update({'font.size': FONT_SIZE_PIE})

	fig1, ax1 = plt.subplots()
	patches, texts, autotexts = ax1.pie(values, labels=labels,
			colors=colors,
			# explode=explode,
			autopct='%1.1f%%',
			startangle=startangle,
			radius=0.8,
			pctdistance=0.8, # default: 0.6
			labeldistance=1.1, # default: 1
			)
	# for text in texts:
	# 	text.set_color('grey')
	for autotext in autotexts:
		autotext.set_color('white')

	centre_circle = plt.Circle((0,0),0.45,fc='white')
	fig = plt.gcf()
	fig.gca().add_artist(centre_circle)

	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

	# plt.legend(patches, labels, loc='left center', bbox_to_anchor=(-0.1, 1.))

	if title is not None:
		plt.title(title)
	plt.tight_layout()

	plt.savefig(out_file, format=out_file_format)


def plot_hist(series, out_file, out_file_format, 
			  x_label, y_label, num_bins, 
			  title=None, color=None):

	plt.rcParams.update({'font.size': FONT_SIZE_BAR})
	fig, ax = plt.subplots()
	plt.figure()

	n, bins, patches = plt.hist(series, num_bins, color=color)

	plt.xlabel(x_label)
	plt.ylabel(y_label)
	if title is not None:
		plt.title(title)

	target_aspect_ratio = 0.9
	x_min, x_max = plt.gca().get_xlim()
	y_min, y_max = plt.gca().get_ylim()
	aspect_ratio = target_aspect_ratio / (float(y_max - y_min) / (x_max - x_min))
	# print(x_min, x_max, y_min, y_max, aspect_ratio)
	plt.axes().set_aspect(aspect=aspect_ratio)

	plt.tight_layout()
	plt.savefig(out_file, bbox_inches='tight', format=out_file_format)


def plot_stats(stats, output_dir, out_file_format="svg"):
	workbooks = stats["workbooks"]
	columns = stats["columns"]

	# datatypes
	datatypes_total = {dt: sum(methods.values()) for dt, methods in stats["datatypes"].items()}
	# create "other" bucket
	others_threshold_ratio=0.01
	count_total = sum(datatypes_total.values())
	datatypes_total_plot = Counter()
	other_datatypes = []
	for dt, c in datatypes_total.items():
		ratio = float(c) / count_total
		if ratio < others_threshold_ratio:
			datatypes_total_plot["other"] += c
			other_datatypes.append(dt)
			print("{}: percentage={}%".format(dt, ratio * 100))
		else:
			datatypes_total_plot[dt] += c
	# other_label = "other\n(" + "\n".join(other_datatypes[:]) + ")"
	# datatypes_total_plot[other_label] = datatypes_total_plot["other"]
	# del datatypes_total_plot["other"]
	datatypes_total = datatypes_total_plot
	# datatypes colors
	datatypes_colors = {}
	for idx, (dt, count) in enumerate(datatypes_total.most_common()):
		datatypes_colors[dt] = DEFAULT_COLORS[idx]

	# compression methods
	compression_methods = stats["compression_methods"]
	compression_labels = {
		"NoCompressionEstimator": "No compression",
		"RleEstimator": "RLE",
		"ForEstimator": "FOR",
		"DictEstimator": "DICT"
	}
	# compression colors
	compression_colors = {}
	for idx, (method, count) in enumerate(compression_methods["total"].most_common()):
		# color_idx = idx
		color_idx = len(datatypes_colors.keys()) + idx
		compression_colors[method] = DEFAULT_COLORS[color_idx]


	# # table average
	# methods = sorted(compression_methods["table_average"].keys(), key=lambda m: compression_methods["table_average"][m])
	# values = [compression_methods["table_average"][m] for m in methods]
	# labels = [compression_labels[m] for m in methods]
	# colors = [compression_colors[m] for m in methods]
	# out_file = os.path.join(output_dir, "compression_methods_table_average.{}".format(out_file_format))
	# plot_piechart(values, labels,
	# 			  out_file, out_file_format,
	# 			  colors=colors,
	# 			  title=None)

	# table total
	methods = sorted(compression_methods["total"].keys(), key=lambda m: compression_methods["total"][m])
	values = [compression_methods["total"][m] for m in methods]
	labels = [compression_labels[m] for m in methods]
	colors = [compression_colors[m] for m in methods]
	out_file = os.path.join(output_dir, "compression_methods_total.{}".format(out_file_format))
	plot_piechart(values, labels,
				  out_file, out_file_format,
				  colors=colors,
				  title=None,
				  startangle=90)

	# datatypes
	datatypes = sorted(datatypes_total.keys(), key=lambda dt: datatypes_total[dt])
	values = [datatypes_total[dt] for dt in datatypes]
	labels = datatypes
	colors = [datatypes_colors[dt] for dt in datatypes]
	out_file = os.path.join(output_dir, "datatypes_total.{}".format(out_file_format))
	plot_piechart(values, labels,
				  out_file, out_file_format,
				  colors=colors,
				  title=None)

	# number of columns
	values = sorted(columns.values(), key=lambda x: -x)
	x_label, y_label, num_bins = "number of columns", "count (tables)", 20
	title = "Number of columns"
	out_file = os.path.join(output_dir, "column_count.{}".format(out_file_format))
	plot_hist(values, out_file, out_file_format,
			  x_label, y_label, num_bins,
			  # title=title,
			  color=DEFAULT_COLORS[1]
			  )


if __name__ == "__main__":

	analysis_manager = AnalysisManager()

	for d in os.listdir(BENCHMARK_SRC_DIR):
		wb = d

		src_wb_path = os.path.join(BENCHMARK_SRC_DIR, d, "samples")
		if not os.path.isdir(src_wb_path):
			print("error: unexpected file: {}".format(src_wb_path))
			continue

		for f in os.listdir(src_wb_path):
			table = f.split(".")[0]

			linecount_file = os.path.join(src_wb_path, f)
			if not os.path.isfile(linecount_file):
				print("error: unexpected directory: {}".format(linecount_file))
				continue
			if not linecount_file.endswith(".linecount"):
				continue

			evaluation_file = os.path.join(WBS_DIR, "{}/{}.evaluation/{}.eval-theoretical.json".format(wb, table, table))
			if not os.path.isfile(evaluation_file):
				print("error: evaluation file not found: {}".format(evaluation_file))
				continue
			analysis_manager.feed_table(wb, table, evaluation_file)

	stats = analysis_manager.get_stats()
	output_stats(stats, OUTPUT_DIR)
	plot_stats(stats, OUTPUT_DIR, OUT_FILE_FORMAT)
