from Aparato import Aparato
class Lavarropa(Aparato):
    __capacidad=0
    __velocidad=0
    __cantidadPrograma=0
    __tipoCarga=''
    def __init__(self,marca='',modelo='',color='',paisFabricacion='',precio='',capacidad=0,velocidad=0,cantidadPrograma=0,tipoCarga=''):
        super(). __init__(marca,modelo,color,paisFabricacion,precio)
        self.__capacidad=capacidad
        self.__velocidad=velocidad
        self.__cantidadPrograma=cantidadPrograma
        self.__tipoCarga=tipoCarga
    def calcularPorcentaje(self):
        resultado=0
        porcentaje=0
        if self.__capacidad<=5:
            porcentaje+=1
        elif self.__capacidad>5:
            porcentaje+=3
        resultado=(self.getPrecio()*porcentaje)/100
        return resultado
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(super().toJSON(),capacidad=self.__capacidad,velocidad=self.__velocidad,cantidadPrograma=self.__cantidadPrograma,tipoCarga=self.__tipoCarga)
        )
        return d
    def getTipo(self):
        return self.__tipoCarga
        
