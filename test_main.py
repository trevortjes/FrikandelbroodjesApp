from UserInterface import CreateUI
import pytest

@pytest.fixture
def draw_ui():
    return CreateUI()

# Test the calculation for the amount of frikandelbroodjes with different types of inputs
@pytest.mark.parametrize("money, price, expected",[
    (1, 1, 1),
    (1, 2, 0),
    (2, 1, 2),
    (2,-1, -2),
    ("1,5" , "0,5", 3), # can be , or . for delimiter
    ('h', 3, "wrong input")
])

def test_inputs(draw_ui, money, price, expected):
    assert draw_ui.calculate_quantity(money, price) == expected


# Test the textual logic for "Frikandelbroodje(s)"
@pytest.mark.parametrize("value, expected",[
    (1, "broodje"),
    (2, "broodjes"),
    (0, "broodjes"),
    (-1, "invalid"),
])

def test_results(draw_ui, value, expected):
    assert draw_ui.show_result(value) == expected