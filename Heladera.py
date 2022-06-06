from Aparato import Aparato
class Heladera(Aparato):
    __capacidadLitros=0
    __freezer=False
    __ciclica=False
    def __init__(self,marca='',modelo='',color='',paisFabricacion='',precio='',capacidadLitros=0,freezer=False,ciclica=False):
        super(). __init__(marca,modelo,color,paisFabricacion,precio)
        self.__capacidadLitros=capacidadLitros
        self.__freezer=freezer
        self.__ciclica=ciclica
    def calcularPorcentaje(self):
        resultado=0
        porcentaje=0
        if self.__freezer:
            porcentaje+=5
        else:
            porcentaje+=1
        if self.__ciclica:
            porcentaje+=10
        resultado=(self.getPrecio()*porcentaje)/100
        return resultado
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(super().toJSON(),capacidadLitros=self.__capacidadLitros,freezer=self.__freezer,ciclica=self.__ciclica)
        )
        return d