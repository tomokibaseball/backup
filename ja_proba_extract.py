#!/usr/bin/python

import sys

my_file = open(sys.argv[1],"r")
my_dict = {}
for line in my_file:
	line = line.strip()
	
	if len(line) != 0:
		words = line.split("|||")
		word = words[0]
		probability = words[2][0:7]
		my_dict[word] = probability

for key,value in sorted(my_dict.items()):
	print value
	#if value > 0.5000:
		#print key,value 
