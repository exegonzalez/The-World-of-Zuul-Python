

class Item():

    def __init__(self, nombre, descritpion, weight):
        self.__nombre = nombre
        self.__descritpion = descritpion
        self.__weight = weight

    def getName(self):
        return self.__nombre

    def itemInfo(self):
        return self.__nombre+ ': '+ self.__descritpion