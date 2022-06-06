from Menu import Menu
from Lista import Lista
from ObjectEncoder import ObjectEncoder 
if __name__=='__main__':
    objectEncoder=ObjectEncoder()
    lista=None
    archivo='aparatoselectronicos.json'
    diccionario=objectEncoder.leerJSONArchivo('aparatoselectronicos.json')
    if diccionario!=-1:
        lista=objectEncoder.decodificarDiccionario(diccionario)
        print('Se cargaron los datos del archivo')
    else:
        lista=Lista()
    menu=Menu()
    menu.lanzarMenu(lista,objectEncoder)


