class Persona():
    def __init__(self, nom, ape, edad, talla, peso):
        self.__nombre = nom
        self.__apellido = ape
        self.__edad = edad
        self.__talla = talla
        self.__peso = peso

    def procesarEdad(self, edad):
        if(edad > 18):
            resultado = "Es mayor de edad"
        else:
            resultado = "es menor de edad"
        return resultado

    def getnom(self):
        return self.__nombre
    def getape(self):
        return self.__apellido
    def getedad(self):
        return self.__edad
    def gettalla(self):
        return self.__talla
    def getpeso(self):
        return self.__peso

    def setnom(self, nom):
        self.__nombre = nom
    def setape(self, ape):
        self.__apellido = ape
    def setedad(self, edad):
        self.__edad = edad
    def settalla(self, talla):
        self.__talla = talla
    def setpeso(self, peso):
        self.__peso = peso


