#!/usr/bin/env python3
# Get data from file
import re
import sys

file = sys.argv[1]
with open(file) as f:
	for line in f:#lines:
		if "Service" not in line:
			continue
		pattern = r"_(\d+)_(\d+)_(\d+)"
		#print(pattern)
		result = re.search(pattern, line)
		print(result[1]+" "+result[2]+" "+result[3])