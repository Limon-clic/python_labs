import pytest
from unit_35б import *


def test_summ():
    res = summ(1, 3, 6)
    assert res[0] == 7  # ошибка в test_summ - x*y*z
    assert res[1] == 18  # ошибка в test_summ - x+y+z/2


def test_sqrt_maxx():
    assert sqrt_maxx(1, 2) == 4  # ошибка в test_maxx
    assert sqrt_maxx(-2, 4) == 16  # ошибка в test_maxx
    assert sqrt_maxx(-1, -2) == 1  # ошибка в test_maxx


test_summ()
test_sqrt_maxx()
