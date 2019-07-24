#!/usr/bin/env python3

import os
import sys
import json

# NOTE: this is needed when running on remote server through ssh
# see: https://stackoverflow.com/questions/4706451/how-to-save-a-figure-remotely-with-pylab
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
STATS_FILE = os.path.join(SCRIPT_DIR, "output/stats.json")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")

FONT_SIZE_BAR = 19
FONT_SIZE_PIE = 14


def plot_linecount(stats):
	out_file_format = "pdf"
	out_file = os.path.join(OUTPUT_DIR, "rows.{}".format(out_file_format))
	n_bins = 20
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

	plt.rcParams.update({'font.size': FONT_SIZE_BAR})
	fig, ax = plt.subplots()
	plt.figure()

	plt.hist(values, bins=n_bins)

	plt.xlabel("number of rows (millions)")
	plt.ylabel("count (tables)")
	# plt.title("Number of rows")

	target_aspect_ratio = 0.9
	x_min, x_max = plt.gca().get_xlim()
	y_min, y_max = plt.gca().get_ylim()
	aspect_ratio = target_aspect_ratio / (float(y_max - y_min) / (x_max - x_min))
	# print(x_min, x_max, y_min, y_max, aspect_ratio)
	plt.axes().set_aspect(aspect=aspect_ratio)

	plt.tight_layout()
	plt.savefig(out_file, bbox_inches='tight', format=out_file_format)
	plt.close()


if __name__ == "__main__":

	with open(STATS_FILE, 'r') as f:
		stats = json.load(f)

	plot_linecount(stats)
