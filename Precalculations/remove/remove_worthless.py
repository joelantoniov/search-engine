#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
from json import loads

f1 = "worthless.json"
fd = open(f1, 'r', encoding='utf-8')
file_content = fd.read()
result = loads(file_content)

f2 = "ter-VI.txt"
fd2 = open(f2, 'r', encoding='utf-8')
cont = fd2.read()
result2  = [i for i in cont.split('\n')]

for s in result2:
    yn = 0
    s = s.replace(':', "")
    s = s.replace('”', "")
    s = s.replace('“', "")
    s = s.replace('–', "")
    s = s.replace(" ", "")
    s = s.replace("/", "")
    s = s.replace("\\", "")
    s = s.replace("\n", "")
    s = s.replace("\xa0", "")
    s = s.replace("\x9f", "")
    s = s.replace("\x80", "")
    s = s.replace(".", "")
    s = s.replace(",", "")
    s = s.replace("'", "")
    s = s.replace("-", "")
    s = s.replace("+", "")
    s = s.replace("0", "")
    s = s.replace("1", "")
    s = s.replace("2", "")
    s = s.replace("3", "")
    s = s.replace("4", "")
    s = s.replace("5", "")
    s = s.replace("6", "")
    s = s.replace("7", "")
    s = s.replace("8", "")
    s = s.replace("9", "")
    s = s.replace("?", "")
    s = s.replace("¿", "")
    s = s.replace("!", "")
    s = s.replace("¡", "")
    s = s.replace("=", "")
    s = s.replace(")", "")
    s = s.replace("(", "")
    s = s.replace("#", "")
    s = s.replace('"', "")
    s = s.replace('~', "")
    s = s.replace(']', "")
    s = s.replace('[', "")
    s = s.replace('|', "")
    s = s.replace('^', "")
    s = s.replace('¨', "")
    s = s.replace('*', "")
    s = s.replace('Ç', "")
    s = s.replace(';', "")
    s = s.replace('}', "")
    s = s.replace('{', "")
    s = s.replace('%', "")
    s = s.replace('>', "")
    s = s.replace('<', "")
    s = s.replace('@', "")
    s = s.replace("’", "")
    s = s.replace("‘", "")
    s = s.replace("´", "")
    for k in result[0]["less"]:
        if k==s or len(s)>23 or len(s)<3: 
            yn = 1
            break
    if yn==0:
        print(s)
