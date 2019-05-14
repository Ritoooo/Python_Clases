from dos.POO.index import *
class Pincipal():
    cod = int(input("Ingrese el código->"))
    mar = str(input("Ingrese la marca de la Computadora->"))
    col = str(input("Ingrese el color->"))
    pre = float(input("Ingrese el precio->"))

    obj = Computadora(cod, nom, dur, pre, tip)

    print("El cósigo es ->",cod)
    print("La marca es ->",mar)
    print("El color es ->",col)
    reduc = pre*0.10
    print("El precio es ->",reduc)
