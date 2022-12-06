#! /usr/bin/env python
# -*- coding: utf-8 -*-
import snowballstemmer

stemmer = snowballstemmer.stemmer('spanish')
#print(stemmer.stemWord("cargar carga").split())
while True:
    k = raw_input()
    print(stemmer.stemWord(k))
