from Aparato import Aparato
class Televisor(Aparato):
    __tipoPantalla=''
    __pulgada=0
    __tipoDefinicion=''
    __conexion=False
    def __init__(self,marca='',modelo='',color='',paisFabricacion='',precio='',tipoPantalla='',pulgada=0,tipoDefinicion='',conexion=False):
        super(). __init__(marca,modelo,color,paisFabricacion,precio)
        self.__tipoPantalla=tipoPantalla
        self.__pulgada=pulgada
        self.__tipoDefinicion=tipoDefinicion
        self.__conexion=conexion
    def calcularPorcentaje(self):
        resultado=0
        porcentaje=0
        if self.__tipoDefinicion=='SD':
            porcentaje+=1
        elif self.__tipoDefinicion=='HD':
            porcentaje+=2
        elif self.__tipoDefinicion=='FULL HD':
            porcentaje+=3
        if self.__conexion:
            porcentaje+=10
        resultado=(self.getPrecio()*porcentaje)/100
        return resultado
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(super().toJSON(),tipoPantalla=self.__tipoPantalla,pulgada=self.__pulgada,tipoDefinicion=self.__tipoDefinicion,conexion=self.__conexion)
        )
        return d    
