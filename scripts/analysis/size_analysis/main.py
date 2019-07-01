#!/usr/bin/env python3

import os
import sys
import json
from collections import Counter, defaultdict


WBS_DIR = "/scratch/bogdan/tableau-public-bench/data/PublicBIbenchmark-test"
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
BENCHMARK_SRC_DIR = os.path.join(SCRIPT_DIR, "../../../benchmark")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")


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
		self.total_size = 0

	def feed_table(self, wb, table, evaluation_file):
		self.table_count += 1
		with open(evaluation_file, 'r') as f:
			stats = json.load(f)
			size = stats["table"]["data_files"]["size_B"]
		self.workbooks[wb]["tables"][table] = size
		self.total_size += size

	def get_stats(self):
		return {
			"workbooks": self.workbooks,
			"total_size": self.total_size
		}


def output_stats(stats, output_dir):
	out_file = os.path.join(output_dir, "stats.json")
	with open(out_file, 'w') as fp:
		json.dump(stats, fp, indent=2)

	print("[stats] total_size={}".format(sizeof_fmt(stats["total_size"])))


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

			# evaluation_file = os.path.join(WBS_DIR, "{}/{}.evaluation-nocompression/{}.eval-vectorwise.json".format(wb, table, table))
			evaluation_file = os.path.join(WBS_DIR, "{}/{}.evaluation/{}.eval-vectorwise.json".format(wb, table, table))
			if not os.path.isfile(evaluation_file):
				print("error: evaluation file not found: {}".format(evaluation_file))
				continue
			analysis_manager.feed_table(wb, table, evaluation_file)

	stats = analysis_manager.get_stats()
	output_stats(stats, OUTPUT_DIR)
