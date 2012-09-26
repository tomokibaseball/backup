#!/usr/bin/python

import sys
import time
import os


infp = open(sys.argv[1], 'r')

l = infp.readlines()

for line in xrange(len(l)):
	if l[line] != '\n':
		print l[line],  

infp.close()
