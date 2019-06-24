#!/usr/bin/env python3

import os
import sys
import json
from collections import Counter, defaultdict


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
BENCHMARK_SRC_DIR = os.path.join(SCRIPT_DIR, "../../../benchmark")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")


class AnalysisManager(object):
	def __init__(self):
		self.table_count = 0
		self.workbooks = defaultdict(lambda: {
			"tables": dict()
		})

	def feed_table(self, wb, table, linecount_file):
		self.table_count += 1
		with open(linecount_file, 'r') as f:
			linecount = int(f.readline())
		self.workbooks[wb]["tables"][table] = linecount

	def get_stats(self):
		return {
			"workbooks": self.workbooks
		}


def output_stats(stats, output_dir):
	out_file = os.path.join(output_dir, "stats.json")
	with open(out_file, 'w') as fp:
		json.dump(stats, fp, indent=2)


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

			analysis_manager.feed_table(wb, table, linecount_file)

	stats = analysis_manager.get_stats()
	output_stats(stats, OUTPUT_DIR)
