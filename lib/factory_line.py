from lib.toy import Toy

class FactoryLine:
    def __init__(self, type):
        self.type = type
        self.toys = []

    def create_toy(self, toy_name, toy_colour):
        toy = Toy(toy_name, toy_colour)
        self.toys.append(toy)
