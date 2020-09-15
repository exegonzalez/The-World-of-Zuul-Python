
class Room():

    def __init__(self, description):
        self.__description = description
        self.__exits = {}
        self.__item = None # muchos items

    def setExits(self, north, east, south, west, up, down):
        if(north is not None):
            self.__exits['north'] = north
        if(east is not None):
            self.__exits['east'] = east
        if(south is not None):
            self.__exits['south'] = south
        if(west is not None):
            self.__exits['west'] = west
        if(up is not None):
            self.__exits['up'] = up
        if(down is not None):
            self.__exits['down'] = down

    def setExit(self, direccion, room):
        self.__exits[direccion] = room

    def getDescription(self):
        return self.__description
    
    def printLocationInfo(self):
        print("You are stand ", self.getDescription())
        print("Exits:", self.getExitsString())
        print("Items", self.getItems())
        print()

    def getExit(self, direction):
        if(direction in self.__exits):
            return self.__exits[direction]
        else:
            return None

    def getExitsString(self):
        exits = ' | '
        exits = exits.join(self.__exits.keys())
        return exits
    
    #! pensar para muchos items
    def getItems(self):
        items = ''
        if(self.__item is not None):
            items += self.__item.descritpion
        return items

    #! pensar para muchos items
    def addItem(self, item):
        self.__item = item