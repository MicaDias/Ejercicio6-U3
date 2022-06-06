from Heladera import Heladera
from Lavarropa import Lavarropa
from Televisor import Televisor
from Aparato import Aparato
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.opcion5,
            6:self.opcion6,
            7:self.opcion7,
            8:self.salir
        }
    def lanzarMenu(self,lista,objectEncoder):
        #Menu opciones
        i=len(self.__opciones)
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1: Insertar un aparato.')
            print('-Ingrese 2: Agregar un aparato.')
            print('-Ingrese 3: Mostrar un aparato.')
            print('-Ingrese 4: Mostrar cantidad de heladera,televisor,lavarropas,cuya marca es phillips.')
            print('-Ingrese 5: Mostrar la marca de todos los lavarropas que tienen carga superior.')
            print('Ingrese 6: Mostrar para todos los aparatos que la empresa tiene a la venta.')
            print('-Ingrese 7: Almacenar la coleccion Lista en el archivo "aparatoselectronicos.json".')
            print('-Ingrese 8:para salir.')
            opcion=self.cargarNumeroEntero('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion>0 and opcion<7:
                ejecutar(lista)
            elif opcion==7:
                ejecutar(lista,objectEncoder)
            else:
                ejecutar()
    def opcion1(self,lista):
        pos=self.cargarNumeroEntero('Ingrese la posicion que desea guardar el elemento:')
        equipo=self.cargarAparato()
        if equipo!=None:
            if isinstance(equipo,Aparato):
                try:
                    lista.insertarElemento(equipo,pos)
                except IndexError:
                    print('La posicion ingresada es incorrecta')
            else:
                print('no se pudo agregar el elemento.')
        else:
            print('No se hizo ninguna carga')
    def opcion2(self,lista):
        equipo=self.cargarAparato()
        if isinstance(equipo,Aparato):
            lista.agregarElemento(equipo)
        else:
            print('No se pudo agregar el elemento.')
        
    def opcion3(self,lista):
        pos=self.cargarNumeroEntero('Ingrese la posicion que desea guardar el elemento:')
        try:
            lista.mostrarElemento(pos)
        except IndexError:
            print('La posicion ingresada es incorrecta.')
    def opcion4(self,lista):
        lista.buscarMarcaPhillips()
    def opcion5(self,lista):
        lista.mostrarLavarropas()
    def opcion6(self,lista):
        lista.mostrarDatosAparatos()
    def opcion7(self,lista,objectEncoder):
       lista.guardarArchivo(objectEncoder)
    def cargarAparato(self):
        equipo=None
        print('******Cargar aparato******')
        numero=self.cargarNumeroEntero('Ingrese 1)-Televisor,2)-Heladera,3)-Lavarropa 4)para salir.')
        if numero!=4:
            if numero==1:
                print('*******Cargar datos del televisor*******')
                marca=input('Ingrese la marca: ')
                modelo=input('Ingrese el modelo: ')
                color=input('Ingrese el color: ')
                pais=input('Ingrese el pais de fabricacion:')
                precio=self.cargarNumeroFlotante('Ingrese el precio base:')
                pantalla=input('Ingrese el tipo de pantalla(crt,vga,plasma,lcd,led):')
                pulgada=self.cargarNumeroEntero('Ingrese la cantidad de pulgadas:')
                tipo=input('Ingrese el tipo de definicion(SD,HD,FULL HD): ')
                conexion=self.cargarBooleano()
                aparato=Televisor(marca,modelo,color,pais,precio,pantalla,pulgada,tipo,conexion)
            elif numero==2:
                print('********Cargar datos de la heladera*******')
                marca=input('Ingrese la marca:')
                modelo=input('Ingrese el modelo:')
                color=input('Ingrese el color:')
                pais=input('Ingrese el pais de fabricacion:')
                precio=self.cargarNumeroFlotante('Ingrese el precio base:')
                capacidadLitros=self.cargarNumeroEntero('Ingrese la capacidad de litros:')
                freezer=self.cargarBooleano()
                ciclica=self.cargarBooleano()
                aparato=Heladera(marca,modelo,color,pais,precio,capacidadLitros,freezer,ciclica)
            else:
                
                print('********Cargar datos del lavarropa*******')
                marca=input('Ingrese la marca:')
                modelo=input('Ingrese el modelo')
                color=input('Ingrese el color')
                pais=input('Ingrese el pais de fabricacion:')
                precio=self.cargarNumeroFlotante('Ingrese el precio base:')
                capacidad=self.cargarNumeroEntero('Ingrese la capacidad:')
                velocidad=self.cargarNumeroEntero('Ingrese la velocidad:')
                cantidadPrograma=self.cargarNumeroEntero('Ingrese la cantidad de programas:')
                tipoCarga=input('Ingrese el tipo de carga:')
                aparato=Lavarropa(marca,modelo,color,pais,precio,capacidad,velocidad,cantidadPrograma,tipoCarga)
            equipo=aparato
        else:
            print('numero incorrecto')
        return equipo
       
        
    def cargarNumeroFlotante(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=float(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero con punto (.), por ejemplo: 10.50')
            else:
                bandera=False
        return numero
    def cargarNumeroEntero(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return numero
    def cargarBooleano(self,mensaje=''):
        resultado=None
        bandera=True
        op=''
        while bandera:
            print(mensaje)
            op=input('Ingrese si(si tiene) o no (no tiene):')
            if op=='si':
                resultado=True
                bandera=False
            elif op=='no':
                resultado=False
                bandera=False
            else:
                print('opcion incorrecta')
                
        return resultado
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')