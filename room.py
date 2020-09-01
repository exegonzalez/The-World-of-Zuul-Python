
class Room():
    def __init__(self, description):
        self.description = description
        self.northExit = None
        self.southExit = None
        self.eastExit = None
        self.westExit = None

    def setExits(self, north, east, south, west):
        if(north is not None):
            self.northExit = north
        if(east is not None):
            self.eastExit = east
        if(south is not None):
            self.southExit = south
        if(west is not None):
            self.westExit = west
        return

    def getDescription(self):
        return self.description
