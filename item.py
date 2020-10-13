

class Item():

    def __init__(self, nombre, descritpion, weight, pickeable, comestible = False, incremento = 0):
        self.__nombre = nombre
        self.__descritpion = descritpion
        self.__weight = weight
        self.__pickeable = pickeable
        
        #! 
        self.__comestible = comestible #! ????
        self.__incremento = incremento

        # self.__danio_magico = 

    def getName(self):
        return self.__nombre

    def itemInfo(self):
        return self.__nombre+ ': '+ self.__descritpion

    def isPickeable(self):
        return self.__pickeable
    
    def getWeight(self):
        return self.__weight
    
    def isComestible(self):
        return self.__comestible