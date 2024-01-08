def entrada():
    n = int(input("Valor de n: "))
    lista = []
    for i in range(n):
        lista.append(i+1)
    print(lista)
    return lista

def busqueda():
    lista = entrada()
    valor_buscado = int(input("Qué número buscas?: "))
    principio_puntero = 0
    final_puntero = len(lista) - 1
    while principio_puntero<= final_puntero:
        valor_actual = (principio_puntero+final_puntero)//2
        if valor_buscado == lista[valor_actual]:
            return valor_actual
        if valor_buscado > lista[valor_actual]:
            principio_puntero = valor_actual + 1
        if valor_buscado < lista[valor_actual]:
            final_puntero = valor_actual - 1
    return None

def main():
    posicion = busqueda()
    if posicion == None:
        return print("El valor buscado no se encuentra en la lista")
    else:
        return print(f"El valor se encuentra en la posición {posicion}")

main()