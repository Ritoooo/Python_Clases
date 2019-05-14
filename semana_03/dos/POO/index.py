class Computadora():
    def __init__(self,cod,mar,col,pre):
        self.__codigo = cod
        self.__marca = mar
        self.__color = col
        self.__precio = pre

    def getcod(self):
        return self.__codigo
    def getmar(self):
        return self.__marca
    def getcol(self):
        return self.__color
    def getpre(self):
        return self.__precio

    def setcod(self,cod):
        self.__codigo = cod
    def setmar(self,mar):
        self.__marca = mar
    def setcol(self,col):
        self.__color = col
    def setpre(self,pre):
        self.__precio = pre

    def getdolares(self):
        dolares = self.__precio * 2.58
        return dolares

    def geteuros(self):
        euros = self.getdolares() * 1.25
        return euros
