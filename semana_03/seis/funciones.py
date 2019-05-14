from seis.POO.index import *
class Principal():
    cod = int(input("Ingrese su código->"))
    nom = input("Ingrese su nombre->")
    sue = float(input("Ingrese su sueldo->"))
    num = int(input("Ingrese su número"))

    obj = Empleado(cod,nom,sue,num)
    print("El código es: ", obj.getcod())
    print("El nombre es: ", obj.getnom())
    print("El sueldo es: ", obj.getsue())
    print("La número es: ", obj.getnum())
    print(obj.compararSueldo(obj.getsue()))