import time                                                                                         #0
import random                                                                                       #0

def N_value():                                                                                      #1
    lista = []                                                                                      #2
    for i in range (100000,1600000,100000):                                                               #1+n+n
        lista.append(i)                                                                             #n
    print(lista)                                                                                    #1
    return lista                                                                                    #1

def Lista(n):                                                                                       #2
    a = 0                                                                                           #2
    b = 500                                                                                         #2
    lista = []                                                                                      #2
    x = n[int(input("Ingrese el tamaño de n elegir entre (0-14):  "))]                              #2
    for i in range(0,x):                                                                            #1+n+n
        lista.append(random.randint(a,b))                                                           #n
    lista.append(x)                                                                                 #1
    print(lista)                                                                                    #1
    return lista                                                                                    #1

def main():
    x = "s"                                                                                         #2
    while x.lower():                                                                                #n
        tamano_lista = N_value()                                                                    #2+n
        lista = Lista(tamano_lista)                                                                 #2+n
        numero = int(input("Ponga el número que desea buscar: "))                                   #2+n
        for j in range(len(lista)-1):                                                               #1+n+n
            if numero==lista[j]:                                                                    #n
                print(f"El número se encuentra en la posicion:{j}")                                 #n
        print("Con un n =", lista[-1]," el tiempo es de: ")                                         #n
        print(time.thread_time())                                                                   #n                                                          #n
        x = input("Desea continuar? (s/n): ")                                                       #n
    
main()                                                                                              #1
#TOTAL : 30+17n