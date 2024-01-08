import random

#Nodo Simple

class Nodo():
    def __init__(self):
        self.sig=None

#Lista Simple Enlazada

class Ls():
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.largo=0
    
    def AgregarUltimo(self, nuevo):
        if self.primero==None:
            self.primero=nuevo
            self.ultimo=nuevo
        else:
            self.ultimo.sig=nuevo
            self.ultimo=nuevo
        self.largo+=1
    
    def AgregarPrimero(self,nuevo):
        if self.primero==None:
            self.AgregarUltimo(nuevo)
        else:
            nuevo.sig=self.primero
            self.primero=nuevo
            self.largo+=1
    
    def Agregar(self,nuevo,pos):
        if self.primero==None:
            self.AgregarUltimo(nuevo)
        elif pos<=0:
            self.AgregarPrimero(nuevo)
        elif pos>self.largo:
            self.AgregarUltimo(nuevo)
        else:
            actual=self.primero
            for p in range(pos-1):
                actual=actual.sig
            nuevo.sig=actual.sig
            actual.sig=nuevo
            self.largo+=1
    
    def Borrar(self,pos):
        if not (0<=pos<self.largo):
            return
        if pos==0:
            objB=self.primero
            if self.primero==self.ultimo:
                self.ultimo=None
            self.primero=self.primero.sig
            del objB
        else:
            actual=self.primero
            for p in range(pos-1):
                actual=actual.sig
            objB=actual.sig
            actual.sig=objB.sig
            if self.ultimo==objB:
                self.ultimo=actual
                actual.sig=None
            del objB
        self.largo-=1
    
    def Azar(self):
        actual=self.primero
        for pos in range(random.randint(0,self.largo-1)):
            actual=actual.sig
        return actual
    
    def __str__(self):
        cadena="["
        actual=self.primero
        while actual is not None:
            cadena+= str(actual)
            cadena+= ","
            actual=actual.sig
        cadena+="]"
        return cadena
    
    def Obtener(self,pos):
        actual=self.primero
        for p in range(pos):
            actual=actual.sig
        return actual

#Nodo Doble

class NodoO(Nodo):
    def __init__(self):
        Nodo.__init__(self)
        self.ant=None

#Lista Doble

class Ld(Ls):
    def __init__(self):
        Ls.__init__(self)
    
    def AgregarUltimo(self, nuevo):
        if self.primero==None:
            self.primero=nuevo
            self.ultimo=nuevo
        else:
            self.ultimo.sig=nuevo
            nuevo.ant=self.ultimo
            self.ultimo=nuevo
        self.largo+=1
    
    def AgregarPrimero(self,nuevo):
        if self.primero==None:
            self.AgregarUltimo(nuevo)
        else:
            nuevo.sig=self.primero
            self.primero.ant=nuevo
            self.primero=nuevo
            self.largo+=1
    
    def Agregar(self,nuevo,pos):
        if self.primero==None:
            self.AgregarUltimo(nuevo)
        elif pos<=0:
            self.AgregarPrimero(nuevo)
        elif pos>self.largo:
            self.AgregarUltimo(nuevo)
        else:
            actual=self.primero
            for p in range(pos-1):
                actual=actual.sig
            nuevo.sig=actual.sig
            nuevo.ant=actual
            actual.sig.ant=nuevo
            actual.sig=nuevo
            self.largo+=1
    
    def Borrar(self,pos):
        if not (0<=pos<self.largo):
            return
        if pos==0:
            objB=self.primero
            if self.primero==self.ultimo:
                self.ultimo=None
            self.primero=self.primero.sig
            self.primero.ant=None
            del objB
        else:
            actual=self.primero
            for p in range(pos-1):
                actual=actual.sig
            objB=actual.sig
            actual.sig=objB.sig
            if actual.sig is not None:
                actual.sig.ant=actual
            if self.ultimo==objB:
                self.ultimo=actual
                actual.sig=None
            del objB
        self.largo-=1
    
    def __str__(self):
        cadena="["
        actual=self.ultimo
        while actual is not None:
            cadena+= str(actual)
            cadena+= ","
            actual=actual.ant
        cadena+="]"
        return cadena
    

#Lista Circular

class Lsc(Ls):
    def __init__(self):
        Ls.__init__(self)
    
    def AgregarUltimo(self, nuevo):
        Ls.AgregarUltimo(self,nuevo)
        self.ultimo.sig=self.primero
        
    def AgregarPrimero(self,nuevo):
        Ls.AgregarPrimero(self,nuevo)
        self.ultimo.sig=self.primero
    
    def Borrar(self,pos):
        if not (0<=pos<self.largo):
            return
        if pos==0:
            objB=self.primero
            if self.primero==self.ultimo:
                self.ultimo=None
            self.primero=self.primero.sig
        else:
            actual=self.primero
            for p in range(pos-1):
                actual=actual.sig
            objB=actual.sig
            actual.sig=objB.sig
            if self.ultimo==objB:
                self.ultimo=actual
        self.ultimo.sig=self.primero
        del objB
        self.largo-=1

#Lista Circular Doble

class Lcd(Ld):
    def __init__(self):
        Ld.__init__(self)
    
    def AgregarUltimo(self, nuevo):
        Ld.AgregarUltimo(self,nuevo)
        self.ultimo.sig=self.primero
        self.primero.ant=self.ultimo
        self.largo+=1
    
    def AgregarPrimero(self,nuevo):
        Ld.AgregarPrimero(self,nuevo)
        self.primero.ant=self.ultimo
        self.ultimo.sig=self.primero
    
    def Borrar(self,pos):
        Ld.Borrar(self,pos)
        if self.largo>0:
            self.primero.ant=self.ultimo
            self.ultimo.sig=self.primero

class Pila(Ls):
    def __init__(self):
        Ls.__init__(self)
    
    def push(self, nuevo):
        self.AgregarUltimo(nuevo)
    
    def pop(self):
        ultimo=self.ultimo
        self.Borrar(self.largo-1)
        return ultimo

class Cola(Ls):
    def __init__(self):
        Ls.__init__(self)
    
    def enq(self,nuevo):
        self.AgregarUltimo(nuevo)
    
    def deq(self):
        primero=self.primero
        self.Borrar(0)
        return primero