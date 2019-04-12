#!/usr/bin/env python3

import os
import sys
import re


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
BENCHMARK_SRC_DIR = os.path.join(SCRIPT_DIR, "../../benchmark")


def mkdir_p(dir_path):
	try:
		os.mkdir(dir_path)
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise e


def rename_columns(src_table_path, dst_table_path):
	regex_col = re.compile(r'^(.*?)"(.*?)" (.*?),?$')

	with open(src_table_path, 'r') as f_s, open(dst_table_path, 'w') as f_o:
		lines = f_s.readlines()

		f_o.write(lines[0])

		cols = list(map(lambda c: c, lines[1:-1]))
		for col_id, c in enumerate(cols):
			m = regex_col.match(c)
			if not m:
				raise Exception("Unable to parse schema file")
			prefix, col_name, datatype = m.group(1), m.group(2), m.group(3)
			col_name_new = "col_{}".format(col_id)
			line_new = "{}\"{}\" {}".format(prefix, col_name_new, datatype)
			if c.strip().endswith(","):
				line_new += ","
			f_o.write(line_new + "\n")

		f_o.write(lines[-1])


if __name__ == "__main__":

	for d in os.listdir(BENCHMARK_SRC_DIR):
		src_wb_path = os.path.join(BENCHMARK_SRC_DIR, d, "tables")
		dst_wb_path = src_wb_path
		if not os.path.isdir(src_wb_path):
			print("error: unexpected file: {}".format(src_wb_path))
			continue

		for f in os.listdir(src_wb_path):
			src_table_path = os.path.join(src_wb_path, f)
			if not os.path.isfile(src_table_path):
				print("error: unexpected directory: {}".format(src_table_path))
				continue
			if not src_table_path.endswith(".sql"):
				print("error: unexpected file: {}".format(src_table_path))
				continue
			if src_table_path.endswith("-renamed.sql"):
				continue

			dst_f = f[:-len(".sql")] + "-renamed.sql"
			dst_table_path = os.path.join(dst_wb_path, dst_f)
			rename_columns(src_table_path, dst_table_path)
