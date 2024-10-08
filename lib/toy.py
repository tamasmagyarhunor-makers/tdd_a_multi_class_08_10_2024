class Toy:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def get_name_and_colour(self):
        return f"{self.name}, {self.colour}"