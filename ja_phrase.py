#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import os

previous_line = "" #前の行の保持 
infp = open(sys.argv[1], 'r')
for line in infp:
     line = line.strip()
     if line != previous_line: 
        print line    
        previous_line = line    
    

infp.close()
