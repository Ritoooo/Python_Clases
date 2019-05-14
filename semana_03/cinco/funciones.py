from cinco.POO.index import *
class Principal():

    cod = int(input("Ingrese el código->"))
    nom = str(input("Ingrese el nombre del Vídeo->"))
    dur = float(input("Ingrese la duración->"))
    pre = float(input("Ingrese el precio->"))
    tip = float(input("Ingrese el tipo de moneda->"))

    obj = Video(cod, nom, dur, pre, tip)

    print("El cósigo es ->",cod)
    print("El nombre del vídeo es ->",nom)
    print("Su duración es ->",dur)
    print("El precio es ->",pre)
    print("El tipo de moneda es ->",tip)

