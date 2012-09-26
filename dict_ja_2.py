#!/usr/bin/env python
# -*- coding: utf-8 -*-
#argv1 : ja_phrase argv2 : txt.ja 

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
    
infp = open(sys.argv[2], 'r')

ret = ""
for sent in infp:
	sent = sent.split()
	for i in range(0,len(sent)):
		pro = float(0)
		pro2 = float(0)
		#
		if ret in my_dict: 
			pro = float(my_dict[ret])		
			if sent[i] in my_dict:
				pro2 = pro*float(my_dict[sent[i]])
				ret = ret + " " + sent[i]
				if ret not in my_dict:
					ret = ret.replace(sent[i],"") 
					if ret != "":
						print ret 
						#print ""
						ret = sent[i]

				elif pro > pro2:
					ret = ret
			elif sent[i] not in my_dict:
				#if ret != "":
				ret = ret + " " + sent[i]
				#print ret			
			else :
				print "error"
		else :
			ret = sent[i]

		
			
infp.close()