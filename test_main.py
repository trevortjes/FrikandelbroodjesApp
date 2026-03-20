from userinterface import CreateUI
from logic import calculate_quantity, format_result
import pytest

# niet nodig? logic onafhankelijk van UI
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

def test_inputs(money, price, expected):
    assert calculate_quantity(money, price) == expected

# Test the textual logic for "Frikandelbroodje(s)"
@pytest.mark.parametrize("value, expected",[
    ("wrong input", "Das geen getal"),
    (2, f"{2} frikandelbroodjes!"),
    (0, f"{0} frikandelbroodjes!"),
    (1, f"{1} frikandelbroodje!")
    (-1, "Lol poor"),
])

def test_results(value, expected):
    assert format_result(value) == expected