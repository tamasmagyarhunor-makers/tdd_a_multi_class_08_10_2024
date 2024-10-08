from lib.factory_line import FactoryLine

def test_factory_line_instantiates_with_attributes():
    factory_line = FactoryLine('balls')
    
    actual_type = factory_line.type
    actual_toys = factory_line.toys

    expected_type = 'balls'
    expected_toys = []

    assert actual_type == expected_type
    assert actual_toys == expected_toys

def test_factory_can_create_a_toy():
    factory_line = FactoryLine('teddies')

    factory_line.create_toy('teddy', 'red')

    actual_size_of_factory_line_toys = len(factory_line.toys)
    actual_toy_name = factory_line.toys[0].name
    actual_toy_colour = factory_line.toys[0].colour

    exepcted_size_of_factory_line_toys = 1
    expected_toy_name = 'teddy'
    expected_toy_colour = 'red'

    assert actual_size_of_factory_line_toys == exepcted_size_of_factory_line_toys
    assert actual_toy_name == expected_toy_name
    assert actual_toy_colour == expected_toy_colour