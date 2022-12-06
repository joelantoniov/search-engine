words_index={}
IDF=[]

def find(str):
	return (str in words_index)


print("paso 0");
index=1
file1=open("all_raiz_compressed.out",'r', encoding='utf-8')
for line in file1:
	line=line[0:-1]
	if(len(line) and find(line)==0):
		IDF+=[0]
		words_index[line]=index
		index=index+1
file1.close()
numero_de_palabras=index-1
print("paso 1");
matriz={}
file2=open("all_raiz.out",'r', encoding='utf-8')
news_index=-1;
TF=[]
maximo=0
for line in file2:
	line=line[0:-1]
	value=words_index.get(line,0)
	if(line=="BEGINBEGINBEGINBEGIN"):
		TF+=[maximo]
		maximo=0
		news_index=news_index+1
	elif(len(line) and value):
		value=value-1
		if(matriz.get((news_index,value),0)==0):
			matriz[news_index,value]=0
			IDF[value]+=1
		matriz[news_index,value]+=1
		if(matriz[news_index,value]>maximo):
			maximo=matriz[news_index,value]
file2.close()
TF+=[maximo]
numero_de_noticias=news_index+1
print("paso 2")
outfile = open("points.txt", "w", encoding="utf-8")
h=0;
for i in sorted(matriz):
	if(h!=i[0]):
		outfile.write('\n')
		h=i[0];
	outfile.write(str(i[0])+' '+str(i[1])+' '+str((matriz[i]*numero_de_noticias)/(TF[i[0]+1]*IDF[i[1]]))+' ')
outfile.close()
print("Numero de Noticias: ",numero_de_noticias)
print("Numero de Palabras: ",numero_de_palabras)
print("Pares: ",len(matriz))
