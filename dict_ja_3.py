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
ret2 = []
length = 0
pro = float(0)
for sent in infp:
	sent = sent.split()
	for i in range(0,len(sent)):
		
		if ret != "": 
			ret = ret + " " + sent[i]
		else:
			ret = sent[i]

		if ret not in my_dict:
			ret = ret.replace(sent[i],"") 
			ret = ret.strip(" ")
			if ret != "" and ret in my_dict: #既知語
				pro = float(my_dict[ret])
				if pro < float(0.2):
					ret2.append(ret)
					for j in range(0,len(ret2)):
						print ret2[j],
					ret2=[]
					#print ret,pro,length
				else:
					length = len(ret2)
					print ret
					ret2=[]

			elif ret != "" and ret not in my_dict: #未知語
				pro = float(0.001)
				#ret2 = ret
				ret2.append(ret)
				for j in range(0,len(ret2)):
					print ret2[j],
				ret2=[]
				#print ret,pro				
			elif ret == "":
				pro = float(0.9999)
			ret = sent[i]
			
	pro = float(my_dict[ret])	
	#ret = ret2 + ret
	length = len(ret2)	
	print ret	
	#print ""
	ret = ""
	ret2=[]
	
			
infp.close()
