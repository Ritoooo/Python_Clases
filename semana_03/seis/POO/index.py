class Empleado():
    def __init__(self, cod, nom, sue, num):
        self.__codigo = cod
        self.__nombre = nom
        self.__sueldo = sue
        self.__numero = num

    def getcod(self):
        return self.__codigo
    def getnom(self):
        return self.__nombre
    def getsue(self):
        return self.__sueldo
    def getnum(self):
        return self.__numero

    def compararSueldo(self):
        if(self.__sueldo > 3500):
            mensaje = "El sueldo es mayor a 3500"
        elif(self.__sueldo == 3500):
            mensaje  = "El sueldo es igual a 3500"
        else:
            mensaje  = "El sueldo es menor a 3500"

