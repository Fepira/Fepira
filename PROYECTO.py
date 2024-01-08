from page_rank import Pg_Rk as P

class TablaHashInvertida:
    def __init__(self):
        self.indice_invertido = {}

    def insertar(self, palabra, id):
        if palabra in self.indice_invertido:
            if id not in self.indice_invertido[palabra]:
                self.indice_invertido[palabra].append(id)
        else:
            self.indice_invertido[palabra] = [id]
            

    def buscar(self, palabra, page_rank):
        resultados = self.indice_invertido.get(palabra.lower(), [])
        resultados.sort(key=lambda x: page_rank.get(x, 0), reverse=True)
        return resultados

t = TablaHashInvertida()

#Importar sistema operativo
import os

#Directorio
path = r"c:/Users/felix/OneDrive/Escritorio/REPOSITORIO_COD/PROYECTO_ALGORITMOS/documentos/documentos"

#Cambiar del directorio
os.chdir(path)

#Diccionario de palabras con una lista de documentos
def read_text_file(file_path,file):   
    with open(file_path, 'r') as f:   
        contenido = f.read() #Leemos el documento
        palabras = contenido.split() #Separamos los caracteres
        palabrass = list(set(palabras))
        for palabra in palabrass: #Recorremos la lista palabras
            palabra_limpia = palabra.strip(",.;()").replace("\n", "") #Eliminamos caracteres no deseados
            file_name = file.replace(".txt","")
            if palabra_limpia:
                t.insertar(palabra_limpia.lower(),int(file_name)) #Si la palabra no existe, agregamos la palabra como llave y creamos un elemento lista, con el nombre del archivo asociado

for file in os.listdir(): #Iteramos a través de todos los archivos en el directorio
    if file.endswith(".txt"): #Verificamos si el archivo está en formato de texto
        file_path = os.path.join(path, file)  #Utilizamos os.path.join para manejar las barras inclinadas en las rutas
        read_text_file(file_path,file) #Llamamos a la función para leer el archivo de texto

print(t.buscar("Nasa",P))





