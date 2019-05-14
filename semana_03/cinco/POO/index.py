class Video():
    def __init__(self, cod, nom, dur, pre, tip):
        self.__codigo = cod
        self.__nombre = nom
        self.__duracion = dur
        self.__precio = pre
        self.__tipocambio = tip

    def getcod(self):
        return self.__codigo
    def getcom(self):
        return self.__nombre
    def getdur(self):
        return self.__duracion
    def getpre(self):
        return self.__precio
    def gettip(self):
        return self.__tipocambio

    def setcod(self, cod):
        self.__codigo = cod
    def setnom(self, nom):
        self.__nombre = nom
    def setdur(self, dur):
        self.__duracion = dur
    def setpre(self, pre):
        self.__precio = pre
    def settip(self, tip):
        self.__tipocambio = tip


    def procesarSoles(self):
        dolares = self.__precio * 0.3
        return dolares