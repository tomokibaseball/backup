#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import os

infp1 = open(sys.argv[1], 'r')
phrase_table = dict()
for line in infp1: 
    line = line.strip()
       # TODO: Short not there Long there
    phrase_table[line] = 1 #追加した
    
    
infp2 = open(sys.argv[2], 'r')

ret = ""
for sent in infp2:
	sent = sent.split()
	for i in range(0,len(sent)):
   
		if ret != "": 
			ret = ret + " " + sent[i]
		else:
			ret = sent[i]
		if ret not in phrase_table:
			ret = ret.replace(sent[i],"") 
			if ret != "":
				print ret 
				ret = sent[i]
       
	print ret 
	print ""
	ret = ""

#f.close()   
infp1.close()
infp2.close()
