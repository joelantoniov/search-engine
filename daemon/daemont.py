from twisted.internet import protocol, reactor
from twisted.protocols import basic
import snowballstemmer
import datetime
import MySQLdb
import sys
from time import time

DATA_DIR = "../data/"
PORT = 8888

print "Cargando matriz ..."
scc=open(DATA_DIR + "points.txt",'r')
cont=0
matriz = []
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
print "Matriz en memoria."

print "Iniciando servicio en puerto: %s" % PORT
class AppProtocol(basic.LineReceiver):
    
    def __init__(self, words):
        self.stemmer = snowballstemmer.stemmer('spanish')
        
    def lineReceived(self, line):
        #self.transport.write(line)
        print "Query: %s" % line
        self.handle_QUERY(line)
        self.transport.loseConnection()
        
    def handle_rootWord(self, word):
        return (self.stemmer.stemWord(word))

    def handle_QUERY(self, palabras):
        startime=time()
        lista=palabras.split()
        st="""SELECT id, categorias FROM palabras WHERE palabra IN ("""
        cont=1;
        num_words=0;
        for palabra in lista:
            p=self.handle_rootWord(palabra);
            if(len(p)>0):
                st+="""'"""+p+"""'"""
                num_words+=1;
                if(cont==len(lista)):
                    st+=') ORDER BY id'
                else:
                    st+=','
                    cont+=1

        #print st
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
                        cursor.execute("""SELECT * FROM noticias WHERE categoria IN ("""+str(temp).replace("[","").replace("]","")+")")
                        #print "SELECT few cats"
                    else:
                        cursor.execute("""SELECT * FROM noticias""")
                        #print "SELECT ALL cats"
                    noticias=cursor.fetchall()
                    #print len(noticias)
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
                    #print (time()-startime)
                    noti.sort()
                    k=len(noti)-1
                    while(k>=0):
                        self.sendLine("%s#%s#%s#%s#%s#%s" % (str(noti[k][0]), str(noti[k][1]), str(noti[k][2]), str(noti[k][3]), str(noti[k][4]), str(noti[k][5])))
                        #print(str(noti[k][0])+" "+str(noti[k][1])+" "+str(noti[k][2])+" "+str(noti[k][3]))
                        k=k-1
                    #NOTI is the sorted output of the news from the minor to the major
                    # DIstancia is the reccurence found on list 
                    # each list a news and each news: 0 is the position, 1 is the distance and 2 is the date
                    # 3 is the tittle, 3 is the url, 5 the category and 4 the body
            db.close()


class AppFactory(protocol.Factory):
    def __init__(self):
        self.words = ""

    def buildProtocol(self, addr):
        return AppProtocol(self)

reactor.listenTCP(PORT, AppFactory())
reactor.run()

