from cinco.POO.index import *
class Principal():

    cod = int(input("Ingrese el código->"))
    nom = str(input("Ingrese el nombre del Vídeo->"))
    dur = float(input("Ingrese la duración->"))
    pre = float(input("Ingrese el precio->"))
    tip = float(input("Ingrese el tipo de moneda->"))

    obj = Video(cod, nom, dur, pre, tip)

    print("El cósigo es ->")
    print("El nombre del vídeo es ->")
    print("Su duración es ->")
    print("El precio es ->")
    print("El tipo de moneda es ->")
    print("El precio en dólares es ->")
