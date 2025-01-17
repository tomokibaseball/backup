#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

f = open('/home/is/tomoki-f/sim/n-gram')
data = f.read()

# counting
words = {}
for line in data.split():
	for word in line.split():
    		words[word] = words.get(word, 0) + 1
# sort by count
frq = [(v,k) for k,v in words.items()]
frq.sort()
frq.reverse()
for count, word in frq:
    print word, count, float(count)/2961
