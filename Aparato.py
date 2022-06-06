import abc 
from abc import ABC
class Aparato(ABC):
    __marca=''
    __modelo=''
    __color=''
    __paisFabricacion=''
    __precio=0.0
    def __init__(self,marca='',modelo='',color='',paisFabricacion='',precio=0.0):
        self.__marca=marca
        self.__modelo=modelo
        self.__color=color
        self.__paisFabricacion=paisFabricacion
        self.__precio=precio
    def calcularPorcentaje():
        pass
    def calcularImporte(self):
        return self.__precio+self.calcularPorcentaje()
    def getPrecio(self):
        return self.__precio
    def getMarca(self):
        return self.__marca
    def toJSON(self):
        return dict(marca=self.__marca,modelo=self.__modelo,color=self.__color,paisFabricacion=self.__paisFabricacion,precio=self.__precio)
    def mostrarDatos(self):
        print('Marca:{},Modelo:{},Pais:{},Importe:{}'.format(self.__marca,self.__modelo,self.__paisFabricacion,self.calcularImporte()))
    