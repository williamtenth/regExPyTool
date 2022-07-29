#!/usr/bin/env python3
# Get data from file
import re
import sys

file = sys.argv[1]
stringValue = sys.argv[2]
stringPattern = sys.argv[3]
print ("Number of arguments:", len(sys.argv), "arguments")
print ("Argument List:", str(sys.argv))
with open(file) as f:
	for line in f:#lines:
		#if stringValue != "none":
		#	continue
		#if stringValue not in line:
		#	continue
		pattern = re.compile(stringPattern)
		# pattern for example _(\d+)_(\d+)_(\d+)
		result = re.search(pattern, line)
		#print("Resultado:",result)
		if result != None:
			print(result.groups())