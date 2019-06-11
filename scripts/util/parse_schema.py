#!/usr/bin/env python3

import os
import sys
import re


def parse_schema(schema_file):
	schema = {}
	regex_col = re.compile(r'^"(.*?)" (.*?),?$')

	with open(schema_file, 'r') as f:
		# ignore create table line
		f.readline()
		cols = list(map(lambda c: c.strip(), f.readlines()[:-1]))

	for col_id, c in enumerate(cols):
		col_id = str(col_id)
		m = regex_col.match(c)
		if not m:
			raise Exception("Unable to parse schema file")
		col_name, datatype = m.group(1), m.group(2)
		schema[col_id] = {
			"col_id": col_id,
			"col_name": col_name,
			"datatype": datatype
		}

	return schema
