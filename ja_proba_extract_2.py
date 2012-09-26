#!/usr/bin/python
# -*- coding: utf-8 -*-
#翻訳結果文をbleuの算出できる型に変更

import sys
import time
import os

my_file = open(sys.argv[1],"r")
my_dict = {}
previous_line = "、"
previous_pro = float(0)
for line in my_file:
	line = line.strip()
	
	if len(line) != 0:
		(word, pro) = line.split("   ")
		fl = float(pro)
		
		if word == previous_line:		
			if fl > previous_pro:
				previous_pro = fl	
		else:
			print previous_line  + "|" + previous_pro
			previous_line = word
			previous_pro = fl
			

