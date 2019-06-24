#!/usr/bin/env python3

import os
import sys
import json
from matplotlib import pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
STATS_FILE = os.path.join(SCRIPT_DIR, "output/stats.json")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")


def plot_linecount(stats):
	out_file = os.path.join(OUTPUT_DIR, "rows.svg")
	out_file_format = "svg"
	n_bins = 100
	most_common_threshold = 10 * (10**6)

	values = []
	most_common, total = 0, 0
	for wb, wb_data in stats["workbooks"].items():
		for table, linecount in wb_data["tables"].items():
			values.append(linecount / (10**6))
			if linecount < most_common_threshold:
				most_common += 1
			total += 1
	print("[stats] tables with less than {} million rows: {} out of {} ({}%)".format(
			most_common_threshold / (10**6), most_common, total, float(most_common) / total * 100))

	fig1, ax1 = plt.subplots()

	ax1.hist(values, bins=n_bins)

	plt.xlabel("Number of rows (millions)")
	plt.ylabel("Number of tables")
	plt.title("Number of rows")
	plt.tight_layout()

	# plt.show()
	plt.savefig(out_file, format=out_file_format)
	plt.close()


if __name__ == "__main__":

	with open(STATS_FILE, 'r') as f:
		stats = json.load(f)

	plot_linecount(stats)
