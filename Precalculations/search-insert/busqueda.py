#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import codecs
import random
import string
import re
import MySQLdb
import snowballstemmer
import json
import sys
from json import loads
from time import time

DATA_DIR = "./"

stemmer = snowballstemmer.stemmer('spanish')

def root_word(s):
    return (stemmer.stemWord(s))

matriz=[]

scc=open(DATA_DIR + "points.txt",'r')
cont=0
for line in scc:
	linea=line.split()
	id_new=int(linea[0])
	matriz+=[{}]
	while(cont<id_new):
		matriz+=[{}]
		cont+=1
	it=1
	while(it<len(linea)):
		matriz[cont][int(linea[it])]=float(linea[it+1])
		it+=3
	cont+=1


while True:
    input_var = raw_input('Ingresa palabras a buscar: ')
    palabras = input_var
    startime=time()
    lista=palabras.split()
    st="""select id,categorias from palabras where palabra in ("""
    cont=1;
    num_words=0;
    for palabra in lista:
        p=root_word(palabra);
        if(len(p)>0):
            st+="""'"""+p+"""'"""
            num_words+=1;
            if(cont==len(lista)):
                st+=') order by id'
            else:
                st+=','
                cont+=1

    if(num_words>0):
        db=MySQLdb.connect(host='127.0.0.1',user='devel',passwd='develdevel',db='search')
        cursor=db.cursor()
        cursor.execute(st)
        id_category=cursor.fetchall()
        if(len(id_category)>0):
            QUERY=[]
            category=set()
            for word in id_category:
                QUERY+=[word[0]]
                temp=word[1].split();
                i=0
                while(i<len(temp)):
                    category.add(temp[i])
                    i+=2;
            if(len(category)>0):
                if(len(category)<6):
                    cursor.execute("""select * from noticias where categoria in ("""+str(temp).replace("[","").replace("]","")+")")
                else:
                    cursor.execute("""select * from noticias""")
                noticias=cursor.fetchall()
                print len(noticias)
                noti=[]
                for n in noticias:
                    AB=0
                    for valu in QUERY:
                        oov=matriz[n[0]].get(valu,0)
                        if(oov!=0):
                            AB+=oov
                    if(AB>0):
                        A=0
                        for w_p in matriz[n[0]]:
                            A+=(matriz[n[0]][w_p])**2
                        dist=AB/((A*len(QUERY))**(0.5))
                        noti+=[[dist,n[1],n[2],n[0],n[3],n[4],n[5]]]
                print (time()-startime)
                noti.sort()
                k=len(noti)-1
                while(k>=0):
                    print(str(noti[k][0])+" "+str(noti[k][1])+" "+str(noti[k][2])+" "+str(noti[k][3]))
                    k=k-1
                #NOTI es el resultado ordenado de las noticias de menor a mayor es decir tenemos q mostrar las que tengan mayor
                # DIstancia es decir que tengan de valor 1 y ahi ya esta todo en noti que es una lista de lista con
                # donde cada lista es una noticia y cada noticia en la posicion 0 es la distancia en la 1 es la fecha en la 2 
                #es el TItulo luego la posicion 3 es su ID, la 4 es su URl y la 5 es categoria y 6 el contenido(cuerpo)
        print "paso 3"
        db.close()
    
