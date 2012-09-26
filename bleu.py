#!/usr/bin/env python
# -*- coding: utf-8 -*-
#翻訳結果文をbleuの算出できる型に変更

import sys
import time
import os

infp = open(sys.argv[1], 'r')
line = infp.readlines()
infp.close()

ret = ""
for sent_str in line:
   
   sent = sent_str.split()
  # print sent
   if sent == []:
      ret = ret + "\n"
      
   for i in range(0,len(sent)):
    
     if ret != "":
        ret = ret + " " + sent[i] 
     else:
        ret = sent[i]
     
   #print ret,

   print ret,
  # print ""    
   ret = ""
  

