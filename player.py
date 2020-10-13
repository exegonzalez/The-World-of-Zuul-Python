
class Player():

    def __init__(self, max_weight = 10):
        self.__name = None
        self.__items = {}
        self.__max_weight = max_weight
        self.__currentRoom = None

    #! modificar para muchos y control de peso
    def setItem(self, item):
        self.__items[item.getName()] = item
    
    def quitItem(self, item_name):
        if(item_name in self.__items):
            item = self.__items[item_name]
            del self.__items[item_name]
            return item
        else:
            return None
    
    def canTake(self, item):
        return item.getWeight() < (self.__max_weight - self.weightItems())
    
    def weightItems(self):
        weight = 0
        for item in self.__items.values():
            weight += item.getWeight()
        return weight

    def getItems(self):
        items = '|'
        items = items.join(self.__items.keys())
        return items

    def setCurrentRoom(self, room):
        self.__currentRoom = room

    def hasItem(self, item_name):
        return item_name in self.__items