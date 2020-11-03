
from stringcolor import cs

class Item():

    def __init__(self, nombre, descritpion, weight, pickeable):
        self.__nombre = nombre
        self.__descritpion = descritpion
        self.__weight = weight
        self.__pickeable = pickeable

    def getName(self):
        return self.__nombre

    def itemInfo(self):
        return self.__nombre+ ': '+ self.__descritpion

    def isPickeable(self):
        return self.__pickeable
    
    def getWeight(self):
        return self.__weight
    
    def inspectItem(self):
        if(self.isPickeable()):
            print(cs(self.itemInfo(), 'red'))
        else:
            print(cs(self.itemInfo(), 'blue'))


class Comestible(Item):
    
    def __init__(self, nombre, descritpion, weight, pickeable, increment):
        super().__init__(nombre, descritpion, weight, pickeable)
        self.__increment = increment
    
    def eat(self, player):
        player.incrementMaxWeigth(self.__increment)
    
    def inspectItem(self):
        print(cs(self.itemInfo(), 'green'))