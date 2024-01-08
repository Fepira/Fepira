class Nodo:
    def __init__(self, key, ady_list):
        self.key = key
        self.ady_list = ady_list
        self.color = ""
        
    def __str__(self):
        return str(self.key)+" "+str(self.ady_list)+" "+str(self.color)

with open("c:/Users/felix/OneDrive/Escritorio/REPOSITORIO_COD/PROYECTO_ALGORITMOS/grafo2.txt", "r") as archivo:
    grafo = {}
    for linea in archivo:
        l = linea.split()
        l = [int(i) for i in l]
        x = l.pop(0)
        grafo[x] = Nodo(x, l)

def contar_enlaces(d):
    #Contamos los enlaces de entrada-------------------------------------------------------------------------------
    for llave, nodo in grafo.items(): #.items() es un método de python que devuelve el par llave/valor de un diccionario
        for otro_nodo in nodo.ady_list:
            d[otro_nodo].append(llave)
    return d
    #--------------------------------------------------------------------------------------------------------------

def diccionario(g):
    d = {}
    for i in g:
        d[i]=[]
    return d

def sumatoria(i,g,e,r):
    suma = 0
    for j in e[i]:
        suma += r[j] / len(g[j].ady_list)
    return suma

def rank(g):
    r = {}
    for i in g:
        r[i] = 1 / len(g)
    return r

def cambios(d,r,g):
    sum = 0
    for i in g:
        sum += abs(d[i] - r[i])
    return sum

def Page_Rank(g):
    e = contar_enlaces(diccionario(g)) 
    Rank = rank(g)
    q = 0.85
    epsilon = 0.001
    while True:
        dicc_rank = {}
        for i in g:
            dicc_rank[i] = (1 - q) + q * sumatoria(i, g, e, Rank)
        cambio = cambios(dicc_rank,Rank,g)
        if cambio < epsilon:
            break
        Rank = dicc_rank.copy()
    return dicc_rank

Pg_Rk = Page_Rank(grafo)

#print(Page_Rank(grafo))

    
