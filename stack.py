

class Stack():

    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        return self.__elements.pop()

    def isEmpty(self):
        return len(self.__elements) == 0