#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import os


    
infp = open(sys.argv[1], 'r')

for sent in infp:
   print sent.count(' ')
      
#f.close()   
infp.close()

