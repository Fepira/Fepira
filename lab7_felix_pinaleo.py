class Nodo:
    def __init__(self, dato, lst):
        self.dato=dato
        self.lst=lst
    
def suma_nodos(nd, ini):
    cont = ini + nd.dato
    for i in nd.lst:
        cont = suma_nodos(i, cont)
    return cont


#Ejemplo 1:
a1 = Nodo(1,[Nodo(2,[]),Nodo(3,[])])
print(suma_nodos(a1,0))
#Ejemplo 2:
a2 = Nodo(1, [Nodo(2, [Nodo(10, []), Nodo(20, []), Nodo(-1, [])]), Nodo(3, []) ] )
print(suma_nodos(a2,100))
#Ejemplo 3
a3 = Nodo(1, [Nodo(2, [Nodo(4, []), Nodo(5, [Nodo(7, []), Nodo(8, []), Nodo(9, [])])]), Nodo(3, [Nodo(6, [])])])
print(suma_nodos(a3,0))
#Ejemplo 4
a4 = Nodo(3,[Nodo(5,[Nodo(3,[]),Nodo(7,[Nodo(3,[])]),Nodo(77,[])]),Nodo(123,[Nodo(99,[Nodo(-987,[])])])])
print(suma_nodos(a4,78))