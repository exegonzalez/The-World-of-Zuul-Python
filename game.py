from room import Room
from parser_commands import Parser

class Game():
    def __init__(self):
        self.createRooms()
        self.parser = Parser()

    def createRooms(self): 
        #crear habitaciones
        entrance = Room("in the entrance bridge of Millenium Falcon")
        cockpit = Room("in the cockpit")
        side_hall = Room("in the side hall")
        circle_path = Room('in the central path of the ship')
        bathroom = Room("in the bathroom")

        gunner_station = Room("in the gunner station")
        engine_room = Room("in the engine room")

        primary_room = Room("in the primary room of the ship")
        secondary_room = Room("in the primary room of the ship")

        conference_room = Room("in the conference room")

        #inicializar salidas north, east, south, west
        cockpit.setExits(None, None, circle_path, None)
        circle_path.setExits(cockpit, bathroom, entrance, side_hall)
        side_hall.setExits(primary_room, side_hall, secondary_room, entrance)
        entrance.setExits(circle_path, side_hall, None, None)
        bathroom.setExits(None, None, None, circle_path)

        engine_room.setExits(None, None, None, None)
        gunner_station.setExits(None, None, None, None)
       
        primary_room.setExits(None, None, side_hall, None)
        secondary_room.setExits(side_hall, None, None, None)

        conference_room.setExits(None, None, None, None)
        

        #lugar de inicio
        self.currentRoom = gunner_station
        
        return

    def play(self):
        self.printWelcome()
        
        finished = False
        while(not finished):
            command = self.parser.getCommand()
            finished = self.processCommand(command)
        print("Thank you for playing.  Good bye.")

    def printWelcome(self):
        print()
        print("Welcome to the Explore Millennium Falcon - A Star Wars Game!")
        print("Explore Millennium Falcon is a new, incredibly adventure game.")
        print("Type 'help' if you need help.")
        print("")
        print("You are " + self.currentRoom.getDescription())
        print("Exits: ")
        if(self.currentRoom.northExit is not None):
            print("north ")
        if(self.currentRoom.eastExit is not None):
            print("east ")
        if(self.currentRoom.southExit is not None):
            print("south ")
        if(self.currentRoom.westExit is not None):
            print("west ")
        print()

    def processCommand(self,command):
        wantToQuit = False

        if(command.isUnknown()):
            print("I don't know what you mean...")
            return False
        
        commandWord = command.getCommandWord()
        if(commandWord == "help"):
            self.printHelp()
        elif(commandWord == "go"):
            self.goRoom(command)
        elif(commandWord == "quit"):
            wantToQuit = self.quit(command)

        return wantToQuit

    def printHelp(self):
        print("You are lost. You are alone. You wander")
        print("around at the millennium falcon.")
        print()
        print("Your command words are:")
        print("   go quit help")

    def goRoom(self,command):
        if(not command.hasSecondWord()):
            print("Go where?")
            return
        
        direction = command.getSecondWord()
        nextRoom = None
        if(direction == "north"):
            nextRoom = self.currentRoom.northExit
        if(direction == "east"):
            nextRoom = self.currentRoom.eastExit
        if(direction == "south"):
            nextRoom = self.currentRoom.southExit
        if(direction == "west"):
            nextRoom = self.currentRoom.westExit
        
        if(nextRoom == None):
            print("There is no door!")
        else:
            self.currentRoom = nextRoom
            print("You are " + self.currentRoom.getDescription())
            print("Exits: ")
            if(self.currentRoom.northExit is not None):
                print("north ")
            if(self.currentRoom.eastExit is not None):
                print("east ")
            if(self.currentRoom.southExit is not None):
                print("south ")
            if(self.currentRoom.westExit is not None):
                print("west ")
            print()

    def quit(self, command):
        if(command.hasSecondWord()):
            print("Quit what?")
            return False
        else:
            return True

g = Game()
g.play()