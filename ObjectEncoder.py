import json
from pathlib import Path
from Lista import Lista
from Lavarropa import Lavarropa
from Heladera import Heladera
from Televisor import Televisor
class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        resultado=None
        if '__class__' not in d:
            resultado=-1
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Lista': 
                aparatos=d['aparatos']
                lista=class_()
                for i in range(len(aparatos)):
                    dAparato=aparatos[i]
                    class_name=dAparato.pop('__class__')
                    class_=eval(class_name)
                    atributos=dAparato['__atributos__']
                    unAparato=class_(**atributos)
                    lista.agregarElemento(unAparato)
            resultado=lista
        return resultado
    def guardarJSONArchivo(self,diccionario,archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    def leerJSONArchivo(self,archivo):
        resultado=-1
        try:
            with Path(archivo).open(encoding="UTF-8") as fuente:
                diccionario=json.load(fuente)
                fuente.close()
        except FileNotFoundError:
            print('El archivo aparatoselectronicos.json no existe, no se cargaron datos')
        else:
            resultado=diccionario
        return resultado
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)