#!/usr/bin/env python3

import os
import sys
import json
import re
from collections import Counter, defaultdict
from util.parse_schema import parse_schema


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
BENCHMARK_SRC_DIR = os.path.join(SCRIPT_DIR, "../../../benchmark")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")


class AnalysisManager(object):
	def __init__(self):
		self.table_count = 0
		self.table_average = defaultdict(int)
		self.workbooks = defaultdict(lambda: {
			"tables": {},
			"agg": defaultdict(int)
		})
		self.column_count = {
			"total": 0,
			"min": float("inf"),
			"max": 0,
		}

	def feed_table(self, wb, table, schema_file):
		self.table_count += 1
		table_stats = Counter()
		schema = parse_schema(schema_file)

		for col_info in schema.values():
			datatype_name = re.split('\(| ', col_info["datatype"])[0]
			table_stats[datatype_name] += 1
			self.workbooks[wb]["agg"][datatype_name] += 1
			self.table_average[datatype_name] += 1

		self.workbooks[wb]["tables"][table] = table_stats

		column_count = len(schema.keys())
		self.column_count["min"] = min(self.column_count["min"], column_count)
		self.column_count["max"] = max(self.column_count["max"], column_count)
		self.column_count["total"] += column_count

	def get_stats(self):
		for datatype_name, count in self.table_average.items():
			self.table_average[datatype_name] = float(count) / self.table_count
		self.column_count["average"] = float(self.column_count["total"]) / self.table_count
		return {
			"table_average": self.table_average,
			"workbooks": self.workbooks,
			"column_count": self.column_count
		}


def output_stats(stats, output_dir):
	out_file = os.path.join(output_dir, "stats.json")
	with open(out_file, 'w') as fp:
		json.dump(stats, fp, indent=2)


if __name__ == "__main__":

	analysis_manager = AnalysisManager()

	for d in os.listdir(BENCHMARK_SRC_DIR):
		wb = d

		src_wb_path = os.path.join(BENCHMARK_SRC_DIR, d, "tables")
		if not os.path.isdir(src_wb_path):
			print("error: unexpected file: {}".format(src_wb_path))
			continue

		for f in os.listdir(src_wb_path):
			table = f.split(".")[0]

			schema_file = os.path.join(src_wb_path, f)
			if not os.path.isfile(schema_file):
				print("error: unexpected directory: {}".format(schema_file))
				continue
			if not schema_file.endswith(".sql"):
				print("error: unexpected file: {}".format(schema_file))
				continue
			if schema_file.endswith("-renamed.sql"):
				continue

			analysis_manager.feed_table(wb, table, schema_file)

	stats = analysis_manager.get_stats()
	output_stats(stats, OUTPUT_DIR)
