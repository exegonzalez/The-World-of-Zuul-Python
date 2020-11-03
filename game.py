from room import Room
from parser_commands import Parser
from item import Item, Comestible
from stack import Stack
from player import Player

class Game():
    def __init__(self):
        self.createRooms()
        self.parser = Parser()
        self.previousRoom = Stack()
        self.player = Player()

    def createRooms(self): 
        #* crear habitaciones
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

        #* inicializar salidas north, east, south, west
        #cockpit.setExits(None, None, circle_path, None, None, None)
        cockpit.setExit('south', circle_path)
        circle_path.setExits(cockpit, bathroom, entrance, side_hall, gunner_station, engine_room)
        side_hall.setExits(primary_room, side_hall, secondary_room, entrance, None, conference_room)
        #entrance.setExits(circle_path, side_hall, None, None, None, None)
        entrance.setExit('north', circle_path)
        entrance.setExit('east', side_hall)

        #bathroom.setExits(None, None, None, circle_path, None, None)
        bathroom.setExit('west', circle_path)

        engine_room.setExits(None, None, None, None, circle_path, None)
        gunner_station.setExits(None, None, None, None, None, circle_path)
       
        primary_room.setExits(None, None, side_hall, None, None, None)
        secondary_room.setExits(side_hall, None, None, None, None, None)

        #conference_room.setExits(None, None, None, None, side_hall, None)
        conference_room.setExit('up', side_hall)

        # carga de items y cargarlas en el su room
        ligthsaber = Item('lightsaber', 'this is a ligthsaber', 1, True)
        blaster = Item('blaster', 'a stormtrooper blaster', 2.5, True)
        casco = Item('helmet', 'a stormtrooper helmet', 5, True)
        book = Item('book','an old book', 0.5, True)
        table = Item('table', 'a table of metal', 25, False)
        cookie = Comestible('cookie', 'a magic cookie', 0.1, True, 5)
        #blaster = Item('blaster', 'a stormtrooper blaster', 2.5, True)

        cockpit.addItem(blaster) 
        cockpit.addItem(casco) 
        cockpit.addItem(table)
        cockpit.addItem(cookie)
        conference_room.addItem(book)
        #conference_room.addItem(table)
        engine_room.addItem(ligthsaber)

        #! lugar de inicio norte
        self.currentRoom = cockpit
        

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
        self.currentRoom.printLocationInfo()

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
        elif(commandWord == 'look'):
            self.look()
        elif(commandWord == 'inventory'):
            self.showInventory()
        elif(commandWord == 'eat'):
            self.eat(command)
        elif(commandWord == 'back'):
            self.goBack()
        elif(commandWord == 'take'):
            self.takeItem(command)
        elif(commandWord == 'drop'):
            self.dropItem(command)
        elif(commandWord == 'inspect'):
            self.inspect(command)

        return wantToQuit

    def printHelp(self):
        print("You are lost. You are alone. You wander")
        print("around at the millennium falcon.")
        print()
        print("Your command words are:")
        #print("   go quit help")
        print(self.parser.show_commands())

    def goRoom(self,command):
        if(not command.hasSecondWord()):
            print("Go where?")
            return
        
        direction = command.getSecondWord()
        nextRoom = self.currentRoom.getExit(direction)
        if(nextRoom == None):
            print("There is no door!")
        else:
            self.previousRoom.push(self.currentRoom)
            self.currentRoom = nextRoom
            self.currentRoom.printLocationInfo()
            self.player.setCurrentRoom(self.currentRoom)
    
    def look(self):
        self.currentRoom.printLocationInfo()
    
    def showInventory(self):
        print('Items in inventory:', self.player.getItems())
        print('Player current weight:', self.player.weightItems())

    def inspect(self, command):
        if(not command.hasSecondWord()):
            print("Take what?")
            return

        item_name = command.getSecondWord()
        
        if(self.currentRoom.hasItem(item_name)):
            item = self.currentRoom.getItem(item_name)
            item.inspectItem()
        else:
            print('no existe ese item en la habitacion')

    def eat(self, command):
        if(not command.hasSecondWord()):
            print("Take what?")
            return

        item_name = command.getSecondWord()
        
        if(self.player.hasItem(item_name)):
            item = self.player.quitItem(item_name)
            if(isinstance(item, Comestible)):
                item.eat(self.player)
            else:
                self.player.setItem(item)
                print('el item no comestible....')
        
    def goBack(self):
        print('go back to the previous room..')
        if(not self.previousRoom.isEmpty()):
            self.currentRoom = self.previousRoom.pop()
            self.currentRoom.printLocationInfo()
        else:
            print("don't go back, you are in the initial position...")

    def takeItem(self, command):
        if(not command.hasSecondWord()):
            print("Take what?")
            return
        
        item_name = command.getSecondWord()
        item = self.currentRoom.quitItem(item_name)
        if(item is not None):
            if(item.isPickeable()):
                if(self.player.canTake(item)):
                    self.player.setItem(item)
                    print('you took the', item.getName())
                else:
                    print('you no have enough strong..')
                    self.currentRoom.addItem(item)
            else:
                self.currentRoom.addItem(item)
                print("the item can't be taked")
        else:
            print(item_name, 'not exists in the current room')

    def dropItem(self, command):
        if(not command.hasSecondWord()):
            print("Take what?")
            return
        
        item_name = command.getSecondWord()
        item = self.player.quitItem(item_name)
        if(item is not None):
            self.currentRoom.addItem(item)
            print('you dropping the', item.getName())
        else:
            print(item_name, 'not exists in your inventory')

    def quit(self, command):
        if(command.hasSecondWord()):
            print("Quit what?")
            return False
        else:
            return True

game = Game()
game.play()