from main import calculate_quantity
import pytest

def test_calculate_quantity():

    GOOD_VALUES = [1,1.26,999999]
    BAD_VALUES = [-1, 'abcdefghik', 'h', None]

    for value in GOOD_VALUES:
        calculate_quantity(value,value)
