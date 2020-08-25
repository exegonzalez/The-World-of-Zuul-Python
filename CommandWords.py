class CommandWords:
    def __init__(self):
        pass

    VALID_COMMANDS = ["go", "quit", "help"]

    def isCommand(self, aString):
        for word in self.VALID_COMMANDS:
            if(word == aString):
                return True
        return False
