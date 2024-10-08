from lib.factory_line import FactoryLine

class ToyFactory():
    def __init__(self, size):
        self.factory_lines = []
        self.size = size

    def create_factory_line(self, factory_line_type):
        factory_line = FactoryLine(factory_line_type)
        self.factory_lines.append(factory_line)

    def count_all_toys(self):
        counter = 0
        for line in self.factory_lines:
            counter += len(line.toys)

        return counter