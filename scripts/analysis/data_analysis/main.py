#!/usr/bin/env python3

import os
import sys
import json
import re
import traceback
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


def parse_unique_values(line):
	re_obj = re.compile(r'^date:(.*?)[ ]+unique values:(.*?)$')
	m = re_obj.match(line)
	if not m:
		return None
	return {
		"unique_values_count": float(m.group(2))
	}

def parse_repetition_factor(line):
	re_obj = re.compile(r'^repetition factor:(.*?)[ ]+unique flag:(.*?) complete flag:(.*?)$')
	m = re_obj.match(line)
	if not m:
		return None
	return {
		"repetition_factor": float(m.group(1)),
		"unique_flag": m.group(2),
		"complete_flag": m.group(3)
	}

def parse_null_count(line):
	re_obj = re.compile(r'^domain:(.*?) histogram cells:(.*?) null count:(.*?)[ ]+value length:(.*?)$')
	m = re_obj.match(line)
	if not m:
		return None
	return {
		"domain": m.group(1),
		"histogram_cells_count": float(m.group(2)),
		"null_ratio": float(m.group(3)),
		"value_length": float(m.group(4))
	}

def parse_unique_chars(line):
	re_obj = re.compile(r'^unique chars: (.*) $')
	m = re_obj.match(line)
	if not m:
		return None
	return {
		"unique_chars": m.group(1).split(" ")
	}

def parse_char_set_densities(line):
	re_obj = re.compile(r'^char set densities: (.*) $')
	m = re_obj.match(line)
	if not m:
		return None
	return {
		"char_set_densities": m.group(1).split(" ")
	}


def parse_statdump_file(statdump_file):
	parse_functions = [
		parse_unique_values,
		parse_repetition_factor,
		parse_null_count,
		parse_unique_chars,
		parse_char_set_densities
	]
	re_first_line = re.compile(r'^\*\*\* statistics for database (.*?) version: (.*?)$')
	re_table = re.compile(r'^\*\*\* table (.*?) rows:(.*?) pages:(.*?) overflow pages:(.*?)$')
	re_column = re.compile(r'^\*\*\* column (.*?) of type (.*?)$')
	tables = defaultdict(lambda: {
		"table_name": None,
		"rows": None,
		"columns": {}
	})

	# parse statdump file
	with open(statdump_file, 'r') as f:
		for l in f:
			if re_first_line.match(l):
				# table line
				l_t = next(f)
				m_t = re_table.match(l_t)
				if not m_t:
					column_name = None
					continue
				table, rows = m_t.group(1), float(m_t.group(2))
				if tables[table]["table_name"] is not None and tables[table]["table_name"] != table:
					print("[error] different table name: {}".format(table))
				else:
					tables[table]["table_name"] = table
				if tables[table]["rows"] is not None and tables[table]["rows"] != rows:
					print("[error] different rows: {}".format(rows))
				else:
					tables[table]["rows"] = rows
				# column line
				l_c = next(f)
				m_c = re_column.match(l_c)
				if not m_c:
					column_name = None
					continue
				column_name, datatype = m_c.group(1),  m_c.group(2)
				tables[table]["columns"][column_name] = {
					"column_name": column_name,
					"datatype": datatype,
					"lines": []
				}
			elif l.startswith("cell:") or l.isspace():
				continue
			elif column_name is not None:
				tables[table]["columns"][column_name]["lines"].append(l)
			else:
				continue

	# parse data lines for each columns
	for table, table_data in tables.items():
		# print(table)
		# print(json.dumps(table_data, indent=2))
		for column_name, column_data in table_data["columns"].items():
			for line in column_data["lines"]:
				for p_f in parse_functions:
					res = p_f(line)
					if res is not None:
						column_data.update(res)
						break
			del column_data["lines"]
			column_data["uniqueness_ratio"] = float(column_data["unique_values_count"]) / table_data["rows"]

	return tables


class AnalysisManager(object):
	def __init__(self):
		self.tables = defaultdict(dict)

	def feed_table(self, wb, table, statdump_file, evaluation_file):
		try:
			statdump_data = parse_statdump_file(statdump_file)
		except Exception as e:
			print("[error] unable to parse statdump file: {}".format(statdump_file))
			traceback.print_exc()
			return

		if table.lower() not in statdump_data:
			print("[error] {} not found in statdump data".format(table))
			traceback.print_exc()
			return
		columns = statdump_data[table.lower()]["columns"]

		with open(evaluation_file, 'r') as f:
			stats = json.load(f)
		for col_id, col_data in stats["columns"].items():
			col_data = deepcopy(col_data["col_data"])

			if col_data["col_name"] not in columns:
				print("[error] {} not found in statdump data".format(col_data["col_name"]))
				continue
			col_data["statdump"] = columns[col_data["col_name"]]

			self.tables[table][col_id] = col_data

	def get_stats(self):
		return {
			"tables": self.tables
		}


def output_stats(stats, output_dir):
	out_file = os.path.join(output_dir, "stats.json")
	with open(out_file, 'w') as fp:
		json.dump(stats, fp, indent=2)

	print("[stats] table_count={}".format(len(stats["tables"].keys())))


def plot_hist(series, out_file, out_file_format, 
			  x_label, y_label, num_bins, 
			  title=None, color=None):

	plt.rcParams.update({'font.size': FONT_SIZE_BAR})
	fig, ax = plt.subplots()
	plt.figure()

	n, bins, patches = plt.hist(series, num_bins, color=color)

	# plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

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
	null_ratio_values, unique_chars_values, uniqueness_ratio_values = [], [], []

	for table, table_data in stats["tables"].items():
		for col_id, col_data in table_data.items():
			datatype_name = get_datatype_name(col_data["datatype"])
			statdump_data = col_data["statdump"]

			null_ratio_values.append(statdump_data["null_ratio"])
			
			if datatype_name == "varchar":
				if "unique_chars" not in statdump_data:
					# print(json.dumps(statdump_data, indent=2))
					print("[error] unique_chars not present: table={}, col_id={}".format(table, col_id))
				else:
					unique_chars_count = len(statdump_data["unique_chars"])
					unique_chars_values.append(unique_chars_count)
					if unique_chars_count > 255:
						print("unique_chars_count={}, table={}, col_id={}".format(len(statdump_data["unique_chars"]), table, col_id))
			
			uniqueness_ratio_values.append(statdump_data["uniqueness_ratio"])

	# null ratio
	x_label, y_label, num_bins = "null ratio", "count (columns)", 20
	title = "Null ratio"
	out_file = os.path.join(output_dir, "null_ratio.{}".format(out_file_format))
	plot_hist(null_ratio_values, out_file, out_file_format,
			  x_label, y_label, num_bins,
			  # title=title,
			  color=DEFAULT_COLORS[0]
			  )

	# [varchar] len(unique_chars)
	x_label, y_label, num_bins = "unique characters (count)", "count (columns)", 20
	title = "Unique characters"
	out_file = os.path.join(output_dir, "unique_chars.{}".format(out_file_format))
	plot_hist(unique_chars_values, out_file, out_file_format,
			  x_label, y_label, num_bins,
			  # title=title,
			  color=DEFAULT_COLORS[2]
			  )

	# [[?]varchar] uniqueness_ratio
	x_label, y_label, num_bins = "uniqueness ratio", "count (columns)", 20
	title = "Uniqueness ratio"
	out_file = os.path.join(output_dir, "uniqueness_ratio.{}".format(out_file_format))
	plot_hist(uniqueness_ratio_values, out_file, out_file_format,
			  x_label, y_label, num_bins,
			  # title=title,
			  color=DEFAULT_COLORS[3]
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

			statdump_file = os.path.join(WBS_DIR, "{}/{}.evaluation/stats-vectorwise/{}.statdump.out".format(wb, table, table))
			if not os.path.isfile(statdump_file):
				print("error: statdump file not found: {}".format(statdump_file))
				continue
			evaluation_file = os.path.join(WBS_DIR, "{}/{}.evaluation/{}.eval-theoretical.json".format(wb, table, table))
			if not os.path.isfile(evaluation_file):
				print("error: evaluation file not found: {}".format(evaluation_file))
				continue
			analysis_manager.feed_table(wb, table, statdump_file, evaluation_file)

	stats = analysis_manager.get_stats()
	output_stats(stats, OUTPUT_DIR)
	plot_stats(stats, OUTPUT_DIR, OUT_FILE_FORMAT)
