from tres.POO.index import *
class Principal():

    cod = input("Ingrese el código->")
    can = int(input("Ingrese la cantidad de Departamentos->"))
    pre = int(input("Ingrese el precio->"))
    dir = str(input("Ingrese la dirección->"))

    miClase = Edificio(cod, can, pre, dir)
    print("El código es: ", miClase.getcod())
    print("La cantidad es: ", miClase.getcan())
    print("El precio es: ", miClase.getpre())
    print("La dirección es: ", miClase.getdir())
    print("El precio total es: ", miClase.cancularPrecio())
