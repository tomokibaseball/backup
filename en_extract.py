#!/usr/bin/python

import sys
my_file = open(sys.argv[1],"r")
for line in my_file:
	line = line.strip()
	
	if len(line) != 0:
		words = line.split("|||")
		print words[1][1:len(words[1])-1]
	
