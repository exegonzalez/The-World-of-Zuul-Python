

class Item():

    def __init__(self, nombre, descritpion, weight):
        self.__nombre = nombre
        self.__descritpion = descritpion
        self.__weight = weight

    def itemInfo(self):
        return 'info item'