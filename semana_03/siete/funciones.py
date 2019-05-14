from siete.POO.index import *
class Principal():
    '''nom = input("Ingrese el nombre->")
    ape = input("Ingrese el nombre->")
    edad = int(input("Ingrese el nombre->"))
    talla = float(input("Ingrese el nombre->"))
    peso = float(input("Ingrese el nombre->"))'''


    miClase = Persona('Nombre', 'Apellido', 19, 1.75, 70.2)
    print("El nombre es: ",miClase.getnom())
    print("El apellido es: ", miClase.getape())
    print("La edad es: ", miClase.getedad())
    print("La talla es: ", miClase.gettalla())
    print("Su peso es: ", miClase.getpeso())
    print(miClase.procesarEdad(miClase.getedad()))