#! /usr/bin/env python
# -*- coding: utf-8 -*-

counter = 0
a = set()
while True:
    k = raw_input()
    if k == "BEGINBEGINBEGINBEGIN" or (k in a):
        continue
    else:
        a.add(k)
        print k
