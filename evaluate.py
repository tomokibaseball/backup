#!usr/bin/python
# argv1 : ja_test_con
import sys

for line in open(sys.argv[1],'r'):
	n=line.count(' ')
	if n > 17:
		print line
