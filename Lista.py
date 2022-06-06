from zope.interface import implementer
from Interface import Interface
from Nodo import Nodo
from Televisor import Televisor
from Heladera import  Heladera
from Lavarropa import  Lavarropa
from Aparato import Aparato

@implementer(Interface)
class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def insertarElemento(self,elemento,pos):
        nodo=Nodo(elemento)
        error=False
        if pos==0:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo=nodo
            self.__actual=self.__comienzo
            self.__tope+=1
        else:
            if self.__comienzo==None:
                error=True
            else:
                i=0
                ant=self.__comienzo
                aux=self.__comienzo
                while aux!=None and i!=pos:
                    ant=aux
                    aux=aux.getSiguiente()
                    i+=1
                if aux==None:
                    error=True
                else:
                    ant.setSiguiente(nodo)
                    nodo.setSiguiente(aux)
                    self.__tope+=1
        if error:
            raise IndexError
    def agregarElemento(self,elemento):
        nodo=Nodo(elemento)
        if self.__comienzo==None:
            self.__comienzo=nodo
            self.__actual=self.__comienzo
        else:
            aux=self.__comienzo
            ant=self.__comienzo
            while aux!=None:
                ant=aux
                aux=aux.getSiguiente()
            ant.setSiguiente(nodo)
        self.__tope+=1

    def mostrarElemento(self,pos):
        error=False
        if self.__comienzo==None:
            error=True
        else:
            i=0
            
            aux=self.__comienzo
            while aux!=None and i!=pos:
                
                aux=aux.getSiguiente()
                i+=1
            if aux==None:
                error=True
            else:
                t=''
                if type(aux.getDato())==Televisor:
                    t='Televisor'
                elif type(aux.getDato())==Heladera:
                    t='Heladera'
                else:
                    t='Lavarropa'
        print('El aparato almacenado en la posicion:{},es:{}'.format(pos,t))
        if error:
            raise IndexError 
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            aparatos=[aparato.toJSON()for aparato in self]
            )
        return d
    def guardarArchivo(self,objectEncoder):
        diccionario=self.toJSON()
        objectEncoder.guardarJSONArchivo(diccionario,'aparatoselectronicos.json')
    def buscarMarcaPhillips(self):
        contar=0
        contarL=0
        contarH=0
        for aparato in self:
            if aparato.getMarca()=='Phillips':
                if type(aparato)==Televisor:
                    contar+=1
                elif type(aparato)==Lavarropa:
                    contarL+=1
                else:
                    contarH+=1
        print('La cantidad de televisores es:{},cantidad de heladeras:{},cantidad de lavarropas:{}'.format(contar,contarH,contarL))
    def mostrarLavarropas(self):
        for aparato in self:
            if type(aparato)==Lavarropa:
                if aparato.getTipo()=='superior':
                    print('La marca de lavarropa con carga superior es:{}'.format(aparato.getMarca()))
    def mostrarDatosAparatos(self):
        for aparato in self:
            aparato.mostrarDatos()