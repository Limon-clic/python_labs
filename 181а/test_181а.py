import pytest
from unit_181а import Class181 as unit


def test_logic():
    u = unit(10)
    arr = [10, 100, 5, -5, 5, 6, 7, 8, 9, 1]
    u.set_arr(arr)
    assert u.logic() == 10 + 100 + 5 - 5 + 5  # ошибка в test_logic


test_logic()
