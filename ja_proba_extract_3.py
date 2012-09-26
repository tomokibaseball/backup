#!/usr/bin/python
# -*- coding: utf-8 -*-
#翻訳結果文をbleuの算出できる型に変更

import sys
import time
import os

my_file = open(sys.argv[1],"r")
my_dict = {}
for line in my_file:
	line = line.strip()
	
	if len(line) != 0:
		(word, pro) = line.split("|")		
		fl = float(pro)
		my_dict[word] = fl
for key,value in sorted(my_dict.items()):
	print key,value 

