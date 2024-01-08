class Nodo:
    def __init__(self,et,tipo):
        self.et=et
        self.tipo=tipo
        self.link=None
    def print(self):
        print("(",self.et,self.tipo,")")

class Pila:
    def __init__(self):
        self.top=None
    def push(self,nodo):
        if self.top==None:
            self.top=nodo
        else:
            nodo.link=self.top
            self.top=nodo
    
    def pop(self):
        if self.top==None:
            aux =self.top
            self.top=self.top.link
            return aux

p=Pila()
texto = "<DOC> <PERSONA> <NOMBRE>Juan</NOMBRE> <APELLIDO>Perez</APELLIDO> <EAD>25</EDAD> <DIRECCION> <CALLE>Los nisperos</CALLE> 1234</NUMERO> </DIRECCION> </PERSONA> <PERSONA> <NOMBRE>Pedro</NOMBRE> <APELLIDO>Gonzalez</APELLIDO> <EDAD>23</EDAD> <DIRECCION> <CALLE>Los mioporos</CALLE> </DIRECCION> </PERSONA> </DOC>"
val = "sig"
n = len(texto)
for i in range(n-1):
    t = texto[i]
    if val =="sig" and t=="<":
        val = "leer"
        et = ""
        if t[i+1]=="/":
            tipo = "cierre"
        else:
            tipo = "apertura"
    elif val=="leer":
        if t==">":
            if tipo=="apertura":
                p.push(Nodo(et,tipo))
            else:
                aux = p.pop()
                if aux==None:
                    