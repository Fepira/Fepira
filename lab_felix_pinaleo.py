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
        if self.top!=None:
            aux =self.top
            self.top=self.top.link
            return aux

p = Pila()
texto="<DOC> <PERSONA> <NOMBRE>Juan</NOMBRE> <APELLIDO>Perez</APELLIDO> <EAD>25</EDAD> <DIRECCION> <CALLE>Los nisperos</CALLE> 1234</NUMERO> </DIRECCION> </PERSONA> <PERSONA> <NOMBRE>Pedro</NOMBRE> <APELLIDO>Gonzalez</APELLIDO> <EDAD>23</EDAD> <DIRECCION> <CALLE>Los mioporos</CALLE> </DIRECCION> </PERSONA> </DOC>"
st = "sig"
n = len(texto)
for i in range(n):
    t = texto[i]
    if st == "sig" and t=="<":
        st="lee"
        lab=""
        if texto[i+1]=="/":
            tipo="cierre"
        else:
            tipo="apertura"
    elif st=="lee":
        if t==">":
            if tipo=="apertura":
                p.push(Nodo(lab,tipo))
            else:
                aux=p.pop()
                if aux==None:
                    print("Parser error, sobra la etiqueta", lab,tipo)
                    break
                if aux.et!=lab:
                    print("Parser error, no coincide etiqueta",lab)
                    break
            tipo=""
            st="sig"
        elif t!="/":
            lab +=t
    if p.top==None:
        print("Sintaxis OK")
    else:
        print("Error")