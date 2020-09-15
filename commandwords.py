
class CommandWords():
    
    def __init__(self):
        pass

    __VALID_COMMANDS = ["go", "look", "quit", 'eat', "help"]

    def isCommand(self, aString):
        return aString in self.__VALID_COMMANDS

    def show_all(self):
        commands = ''
        for command in self.__VALID_COMMANDS:
            commands += command + " "
        return commands