
class Player():

    def __init__(self):
        self.__name = None
        self.__item = None #! modificar para muchos
        #! valor del peso maximo

    #! modificar para muchos y control de peso
    def setItem(self, item):
        self.__item = item
    
    def getItem(self):
        return self.__item