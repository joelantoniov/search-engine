#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
from json import loads

file_name = "turismoViajeros.json"
fd = open(file_name, 'r', encoding='utf-8')
file_content = fd.read()
result = loads(file_content)
count = 0

def with_json():
    with open("words_news.json", "w", encoding="utf-8") as outfile:
        outfile.write('[\n')
        for news in result:
            words = set()
            words = words.union(i.strip() for i in ((news['titulo'].lower()).replace("\\","")).split(" "))
            words = words.union(i.strip() for i in ((news['noticia'].lower()).replace("\\","")).split(' '))
            outfile.write('{\n')
            outfile.write('"noticia"')
            outfile.write(':')
            outfile.write(str(list(words)))
            outfile.write('},\n\n')
        outfile.write(']')


def without_json():
    count = 0
    with open("ter-VI.txt", "w", encoding="utf-8") as outfile:
        for news in result:
           try:
               s = "BEGINBEGINBEGINBEGIN\n"
               outfile.write(s)
               for i in ((news['Titulo'].lower()).replace("\\","")).split(' '): 
                   outfile.write(i +"\n")
               for i in ((news['Noticia'].lower()).replace("\\","")).split(' '): 
                   outfile.write(i+"\n")
               s = "Noticia" + str(count)
           except: continue
without_json()
