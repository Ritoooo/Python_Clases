class Edificio():
    def __init__(self, cod, can, pre, dir):
        self.__codigo = cod
        self.__cantidad = can
        self.__precio = pre
        self.__direccion =  dir

    def getcod(self):
        return self.__codigo
    def getcan(self):
        return self.__cantidad
    def getpre(self):
        return self.__precio
    def getdir(self):
        return self.__direccion

    def setcod(self, cod):
        self.__codigo = cod
    def setcan(self, can):
        self.__cantidad = can
    def setpre(self, pre):
        self.__precio = pre
    def setdir(self, dir):
        self.__direccion = dir


    def cancularPrecio(self):
        precio = self.getcan() * self.getpre()
        return precio