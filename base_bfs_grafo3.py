# Algoritmos, sección Dario Rojas
#Clase que permite reunir key, lista adyacencia y color 
class Nodo:
    def __init__(self, key, ady_list):
        self.key = key
        self.ady_list = ady_list
        self.color = ""
        
    def __str__(self):
        return str(self.key)+" "+str(self.ady_list)+" "+str(self.color)

#------------------------------------------- CON EL ARCHIVO TXT -------------------------------------------------

# with open("./lab_8/archivo.txt", "r") as archivo:
#     grafo = {}
#     for linea in archivo:
#         l = linea.split()
#         l = [int(i) for i in l]
#         x = l.pop(0)
#         grafo[x] = Nodo(x, l)

#------------------------------------------- CON EL CÓDIGO BASE -------------------------------------------------

#Llenamos las lista de adyacencia, usamos un diccionario
#Cargar aquí el archivo con la especificación del grafo
grafo = {}
grafo[0] = Nodo(0, [0, 2])
grafo[1] = Nodo(1, [1, 3, 2, 0])
grafo[2] = Nodo(2, [1])
grafo[3] = Nodo(3, [])
grafo[4] = Nodo(4, [3, 4, 2])


#BFS - DEBE USAR COMO BASE ESTA FUNCION PARA CONSTRUIR LA FUNCION TRAYECTORIA
def bfs(grafo, inicio):
    #Cada nodo del grafo se establece de color blanco
    for i in grafo:
        grafo[i].color = "white"

    cola = []
    cola.append(grafo[inicio])

    while len(cola)>0:
        u = cola.pop(0)
        for v in u.ady_list:
            if v!=u.key and grafo[v].color == "white":
                #grafo[v].color = "gray"  me di cuenta que esta linea es innecesaria
                cola.append(grafo[v])
        u.color = "black"

def trayectoria(grafo, inicio, fin):
    x=bfs(grafo, inicio)
    
    if grafo[fin].color=="black":
        return True
    else:
        return False


inicio = int(input("Seleccione un Nodo de inicio desde 0 a 99: "))
fin = int(input("Ingrese un nodo objetivo: "))
if trayectoria(grafo,inicio,fin)==True:
    print("El nodo es accesible")
else:
    print("El nodo no es accesible")
#LLAMAMOS A LA FUNCION (asume nodo inicial 0)  


    


