class Trabajador():
    def __init__(self, cod, nom, ht, tar):
        self.__codigo = cod
        self.__nombre = nom
        self.__horas = ht
        self.__tarifa = tar

    def getcod(self):
        return self.__codigo
    def getnom(self):
        return self.__nombre
    def getht(self):
        return self.__horas
    def gettar(self):
        return self.__tarifa

    def setcod(self, cod):
        self.__codigo = cod
    def setnom(self, nom):
        self.__nombre = nom
    def setht(self, ht):
        self.__horas = ht
    def settar(self, tar):
        self.__tarifa = tar


    def sueldoBruto(self):
        sueldo = self.getht() * self.gettar()
        return sueldo

    def calcularDescuento(self):
        descuento = self.sueldoBruto() * 0.15
        return descuento

    def sueldoNeto(self):
        sueldo = self.sueldoBruto()-self.calcularDescuento()
        return sueldo
