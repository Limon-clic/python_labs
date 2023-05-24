import pytest
from unit_336а import *


def test_factotial():
    assert factotial(5, 7, 120) == 5040  # ошибка в factotial(0, 5)


def test_mult():
    assert mult(-3, 5) == 0  # ошибка в mult(-3, 5)
    assert mult(-6, -2) == -720  # ошибка в mult(-6, -2)
    assert mult(4, 10) == 604800  # ошибка в mult(4, 10)


def test_logic():
    assert round(logic(5, 7), 3) == 10.294
    assert round(logic(1, 70), 3) == 72
    assert round(logic(15, 4), 3) == 7.169


test_logic()
test_factotial()
test_mult()
