import pytest

from part2 import find_highest_voltage_cell_index

def test_find_highest_voltage_cell_index():
    assert find_highest_voltage_cell_index("811111111111119", 0, 14) == 14
