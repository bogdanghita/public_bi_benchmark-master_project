#!/usr/bin/env python3

import os
import sys
import json
from collections import Counter, defaultdict

# NOTE: this is needed when running on remote server through ssh
# see: https://stackoverflow.com/questions/4706451/how-to-save-a-figure-remotely-with-pylab
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

WBS_DIR = "/scratch/bogdan/tableau-public-bench/data/PublicBIbenchmark-test"
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
BENCHMARK_SRC_DIR = os.path.join(SCRIPT_DIR, "../../../benchmark")
BENCHMARK_SRC_DIR_cwida = "/scratch/bogdan/master-project/public_bi_benchmark/benchmark"
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")

# FONT_SIZE_BAR = 8
FONT_SIZE_BAR = 19
FONT_SIZE_PIE = 14
DEFAULT_COLORS = plt.rcParams['axes.prop_cycle'].by_key()['color']
OUT_FILE_FORMAT = "pdf"


def to_gib(b):
	return float(b) / 1024 / 1024 / 1024


def sizeof_fmt_basic(num):
	for unit in ['','K','M','G','T','P','E','Z']:
		if abs(num) < 1000.0:
			return "%.1f%s" % (num, unit)
		num /= 1000.0
	return "%.1f%s" % (num, 'Y')

def sizeof_fmt(num, suffix='B'):
	for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
		if abs(num) < 1024.0:
			return "%.1f%s%s" % (num, unit, suffix)
		num /= 1024.0
	return "%.1f%s%s" % (num, 'Yi', suffix)


class AnalysisManager(object):
	def __init__(self):
		self.table_count = 0
		self.workbooks = defaultdict(lambda: {
			"tables": dict()
		})
		self.total_size = dict(vw=0, csv=0)

	def feed_table(self, wb, table, evaluation_file, csv_file):
		self.table_count += 1

		# vw size
		with open(evaluation_file, 'r') as f:
			stats = json.load(f)
			size_vw = stats["table"]["data_files"]["size_B"]
		# csv size
		size_csv = os.path.getsize(csv_file)

		self.workbooks[wb]["tables"][table] = {
			"vw": size_vw,
			"csv": size_csv
		}
		self.total_size["vw"] += size_vw
		self.total_size["csv"] += size_csv

	def get_stats(self):
		return {
			"workbooks": self.workbooks,
			"total_size": self.total_size
		}


def output_stats(stats, output_dir):
	out_file = os.path.join(output_dir, "stats.json")
	with open(out_file, 'w') as fp:
		json.dump(stats, fp, indent=2)

	print("[stats] total_size_vw={}, total_size_csv={}".format(
			sizeof_fmt(stats["total_size"]["vw"]),
			sizeof_fmt(stats["total_size"]["csv"])
			))


def plot_size(series, out_file, out_file_format, 
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
	labels, sizes = zip(*sorted([(t, s) for wb, wb_data in workbooks.items() for t, s in wb_data["tables"].items()], key=lambda x: x[0]))
	# print(len(sizes), sizes)
	# print(len(labels), labels)

	vw_size_gb = [to_gib(s["vw"]) for s in sizes]
	csv_size_gb = [to_gib(s["csv"]) for s in sizes]

	x_label = "size (GiB)"
	y_label = "count (tables)"
	title = "Data size distribution"
	num_bins = 20

	out_file = os.path.join(output_dir, "size_vw.{}".format(out_file_format))
	plot_size(vw_size_gb, out_file, out_file_format,
			  x_label, y_label, num_bins,
			  # title=title,
			  color=DEFAULT_COLORS[2]
			  )
	
	out_file = os.path.join(output_dir, "size_csv.{}".format(out_file_format))
	plot_size(csv_size_gb, out_file, out_file_format,
			  x_label, y_label, num_bins,
			  # title=title,
			  color=DEFAULT_COLORS[2]
			  )


def dump_thesis_stats(stats, output_dir):
	workbooks = stats["workbooks"]

	latex_out_file = os.path.join(output_dir, "latex.out")
	with open(latex_out_file, "w") as lfp:

		nb_tables_total = 0
		nb_columns_total = 0
		nb_queries_total = 0
		nb_rows_total = 0
		size_csv_total = 0

		for wb, wb_data in sorted(workbooks.items(), key=lambda x: x[0]):
			# name, #tables, #columns, #rows, #queries, size csv
			name = wb
			nb_tables = len(wb_data["tables"].keys())
			nb_columns, nb_rows, csv_size = 0, 0, 0

			src_wb_path = os.path.join(BENCHMARK_SRC_DIR, wb)
			src_wb_path_cwida = os.path.join(BENCHMARK_SRC_DIR_cwida, wb)

			for table, table_data in sorted(wb_data["tables"].items(), key=lambda x: x[0]):
				csv_size += table_data["csv"]
				
				schema_file = os.path.join(src_wb_path, "tables", "{}.table.sql".format(table))
				with open(schema_file, "r") as f:
					lines = f.readlines()
					nb_columns_t = len(lines) - 2
				
				linecount_file = os.path.join(src_wb_path, "samples", "{}.linecount".format(table))
				with open(linecount_file, "r") as f:
					nb_rows_t = int(f.read())

				nb_columns += nb_columns_t
				nb_rows += nb_rows_t

				# print(wb, table, nb_columns, nb_rows, csv_size)

			queries_dir = os.path.join(src_wb_path_cwida, "queries")
			queries_list = [q for q in os.listdir(queries_dir) if os.path.isfile(os.path.join(queries_dir, q))]
			nb_queries = len(queries_list)

			nb_tables_total += nb_tables
			nb_columns_total += nb_columns
			nb_queries_total += nb_queries
			nb_rows_total += nb_rows
			size_csv_total += csv_size

			latex_row = "{} & {} & {} & {} & {} & {} \\\\".format(name, 
				  							  nb_tables, 
				  							  nb_columns, 
				  							  sizeof_fmt_basic(nb_rows), 
				  							  nb_queries, 
				  							  sizeof_fmt(csv_size))
			lfp.write(latex_row + "\n")
			# print(name, 
			# 	  nb_tables, 
			# 	  nb_columns, 
			# 	  sizeof_fmt_basic(nb_rows), 
			# 	  nb_queries, 
			# 	  sizeof_fmt(csv_size)
			# )

		latex_row = '{} & {} & {} & {} & {} & {} \\\\'.format("Total", 
										  nb_tables_total, 
										  nb_columns_total, 
										  sizeof_fmt_basic(nb_rows_total), 
										  nb_queries_total, 
										  sizeof_fmt(size_csv_total))
		lfp.write(latex_row + "\n")
		print("nb_tables_total={}, nb_columns_total={}, nb_queries_total={}, nb_rows_total={}, size_csv_total={}".format(
				nb_tables_total, 
				nb_columns_total, 
				sizeof_fmt_basic(nb_rows_total), 
				nb_queries_total, 
				sizeof_fmt(size_csv_total))
		)
		print("nb_workbooks", len(workbooks.keys()))


if __name__ == "__main__":

	analysis_manager = AnalysisManager()

	for d in os.listdir(BENCHMARK_SRC_DIR_cwida):
		wb = d

		src_wb_path = os.path.join(BENCHMARK_SRC_DIR_cwida, d, "samples")
		if not os.path.isdir(src_wb_path):
			print("error: unexpected file: {}".format(src_wb_path))
			continue

		for f in os.listdir(src_wb_path):
			table = f.split(".")[0]

			sample_file = os.path.join(src_wb_path, f)
			if not os.path.isfile(sample_file):
				print("error: unexpected directory: {}".format(sample_file))
				continue
			if not sample_file.endswith(".sample.csv"):
				continue

			evaluation_file = os.path.join(WBS_DIR, "{}/{}.evaluation-nocompression/{}.eval-vectorwise.json".format(wb, table, table))
			csv_file = os.path.join(WBS_DIR, "{}/{}.csv".format(wb, table))
			# evaluation_file = os.path.join(WBS_DIR, "{}/{}.evaluation/{}.eval-vectorwise.json".format(wb, table, table))
			if not os.path.isfile(evaluation_file):
				print("error: evaluation file not found: {}".format(evaluation_file))
				continue
			if not os.path.isfile(csv_file):
				print("error: CSV file not found: {}".format(csv_file))
				continue
			analysis_manager.feed_table(wb, table, evaluation_file, csv_file)

	stats = analysis_manager.get_stats()
	output_stats(stats, OUTPUT_DIR)
	plot_stats(stats, OUTPUT_DIR, OUT_FILE_FORMAT)
	dump_thesis_stats(stats, OUTPUT_DIR)
