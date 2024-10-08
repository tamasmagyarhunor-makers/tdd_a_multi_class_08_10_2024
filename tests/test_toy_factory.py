from lib.toy_factory import ToyFactory
from lib.factory_line import FactoryLine

def test_toy_factory_instantiates_with_attributes():
    factory = ToyFactory(10)

    actual_factory_lines = factory.factory_lines
    actual_size = factory.size

    expected_factory_lines = []
    expected_factory_size = 10

    assert actual_factory_lines == expected_factory_lines
    assert actual_size == expected_factory_size

def test_toy_factory_can_count_all_toys_in_its_toys_in_its_factory_lines():
    factory_line = FactoryLine('teddies')

    factory_line.create_toy('teddy', 'red')
    factory_line.create_toy('teddy', 'purple')

    factory_line_2 = FactoryLine('balls')

    factory_line.create_toy('ball', 'red')

    toy_factory = ToyFactory(10)
    toy_factory.factory_lines.append(factory_line)
    toy_factory.factory_lines.append(factory_line_2)

    actual = toy_factory.count_all_toys()

    expected = 3

    assert actual == expected