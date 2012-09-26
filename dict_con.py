#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import os

infp = open(sys.argv[1], 'r')

ret = ""
for sent in infp:
   sent = sent.split()
for i in range(0,len(sent)):
   
   time.sleep(1)
   if sent[i] != "。": 
    ret = ret + " " + sent[i] 
   else:
    print ret + " " + sent[i]
    ret = ""

infp.close()
