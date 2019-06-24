#!/usr/bin/env python3

import os
import sys
import json
from matplotlib import pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
STATS_FILE = os.path.join(SCRIPT_DIR, "output/stats.json")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")


def plot_datatypes(stats):
	out_file = os.path.join(OUTPUT_DIR, "datatypes.svg")
	out_file_format = "svg"

	items = sorted(stats["table_average"].items(), key=lambda x: -x[1])
	print(items)

	other_count = 5
	explode_factor = 0.03
	labels, values, explode = [], [], []
	for l, v in items[:-other_count]:
		labels.append(l)
		values.append(v)
		explode.append(explode_factor if l == "varchar" else 0)
	l_other, v_other = "other", 0
	for l, v in items[other_count:]:
		v_other += v
	labels.append(l_other)
	values.append(v_other)
	explode.append(0)

	fig1, ax1 = plt.subplots()
	ax1.pie(values, labels=labels,
			explode=explode,
			autopct='%1.1f%%',
			# startangle=90,
			)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

	plt.title("Average data type distribution")
	plt.tight_layout()

	# plt.show()
	plt.savefig(out_file, format=out_file_format)
	plt.close()


def plot_column_count(stats):
	out_file = os.path.join(OUTPUT_DIR, "columns.svg")
	out_file_format = "svg"
	n_bins = 100
	most_common_threshold = 80

	values = []
	most_common, total = 0, 0
	for wb, wb_data in stats["workbooks"].items():
		for table, table_data in wb_data["tables"].items():
			column_count = sum(table_data.values())
			values.append(column_count)
			if column_count < most_common_threshold:
				most_common += 1
			total += 1
	print("[stats] tables with less than {} columns: {} out of {} ({}%)".format(
			most_common_threshold, most_common, total, float(most_common) / total * 100))

	fig1, ax1 = plt.subplots()

	ax1.hist(values, bins=n_bins)

	plt.xlabel("Number of columns")
	plt.ylabel("Number of tables")
	plt.title("Number of columns")
	plt.tight_layout()

	# plt.show()
	plt.savefig(out_file, format=out_file_format)
	plt.close()


if __name__ == "__main__":

	with open(STATS_FILE, 'r') as f:
		stats = json.load(f)

	plot_datatypes(stats)
	plot_column_count(stats)
