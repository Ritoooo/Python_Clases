from cuatro.POO.index import *
class Pincipal():
    miClase = Obrero(1, "Roberto", 15, 10.0)
    print("El código es: ", miClase.getcod())
    print("El nombre es: ", miClase.getnom())
    print("Las horas trabajadas es: ", miClase.getht())
    print("Las tarifa por hora es: ", miClase.gettar())
    print("El sueldo bruto es: ", miClase.sueldoBruto())
    print("El descuento EPS es: ", miClase.calcularDescuentoEPS())
    print("El descuento AFP es: ", miClase.calcularDescuentoAFP())
    print("El sueldo neto es: ", miClase.sueldoNeto())