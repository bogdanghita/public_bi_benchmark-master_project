#!/usr/bin/env python3

import os
import sys
import json
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

FONT_SIZE_BAR = 8
FONT_SIZE_PIE = 14
DEFAULT_COLORS = plt.rcParams['axes.prop_cycle'].by_key()['color']
OUT_FILE_FORMAT = "pdf"


class AnalysisManager(object):
	def __init__(self):
		self.table_count = 0
		self.workbooks = defaultdict(lambda: {
			"tables": dict()
		})
		# TODO

	def feed_table(self, wb, table, evaluation_file):
		self.table_count += 1
		compression_method_counter = Counter()

		with open(evaluation_file, 'r') as f:
			stats = json.load(f)
		columns = stats["columns"]

		for col_id, col_data in columns.items():
			data_file = col_data["data_files"]["data_file"]
			compression_method = data_file["compression"]
			compression_method_counter[compression_method] += 1

		self.workbooks[wb]["tables"][table] = compression_method_counter

	def get_stats(self):
		total = sum([t_data for wb, wb_data in self.workbooks.items() for t, t_data in wb_data["tables"].items()], Counter())
		table_average = deepcopy(total)
		for compression_method, count in table_average.items():
			table_average[compression_method] = count / self.table_count

		return {
			"workbooks": self.workbooks,
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

	print("[stats] compression_methods={}".format(json.dumps(stats["compression_methods"], indent=2)))


def plot_piechart(values, labels,
			  	  out_file, out_file_format,
			  	  colors=None,
			  	  title=None):
	plt.rcParams.update({'font.size': FONT_SIZE_PIE})

	fig1, ax1 = plt.subplots()
	patches, texts, autotexts = ax1.pie(values, labels=labels,
			colors=colors,
			# explode=explode,
			autopct='%1.1f%%',
			startangle=90,
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


def plot_stats(stats, output_dir, out_file_format="svg"):
	workbooks = stats["workbooks"]
	compression_methods = stats["compression_methods"]

	compression_labels = {
		"NoCompressionEstimator": "No compression",
		"RleEstimator": "RLE",
		"ForEstimator": "FOR",
		"DictEstimator": "DICT"
	}

	compression_colors = {}
	for idx, (method, count) in enumerate(compression_methods["total"].most_common()):
		compression_colors[method] = DEFAULT_COLORS[idx]

	methods = sorted(compression_methods["table_average"].keys(), key=lambda m: compression_methods["table_average"][m])
	values = [compression_methods["table_average"][m] for m in methods]
	labels = [compression_labels[m] for m in methods]
	colors = [compression_colors[m] for m in methods]
	out_file = os.path.join(output_dir, "compression_methods_table_average.{}".format(out_file_format))
	plot_piechart(values, labels,
				  out_file, out_file_format,
				  colors=colors,
				  title=None)

	methods = sorted(compression_methods["total"].keys(), key=lambda m: compression_methods["total"][m])
	values = [compression_methods["total"][m] for m in methods]
	labels = [compression_labels[m] for m in methods]
	colors = [compression_colors[m] for m in methods]
	out_file = os.path.join(output_dir, "compression_methods_total.{}".format(out_file_format))
	plot_piechart(values, labels,
				  out_file, out_file_format,
				  colors=colors,
				  title=None)


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
