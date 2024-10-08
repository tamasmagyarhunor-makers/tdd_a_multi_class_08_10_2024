from lib.toy import Toy

def test_toy_instantiates_with_name_and_colour():
    toy = Toy('teddy', 'orange')

    actual_name = toy.name
    actual_colour = toy.colour

    expected_name = 'teddy'
    expected_colour = 'orange'

    assert actual_name == expected_name
    assert actual_colour == expected_colour

def test_toy_can_return_name_and_colour():
    toy = Toy('teddy', 'orange')

    actual = toy.get_name_and_colour()

    expected = "teddy, orange"

    assert actual == expected