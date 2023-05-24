import pytest
from unit_115в import *


def test_logic():
    res = round(logic(5), 3)
    assert res == 0.192  # ошибка в logic(5)


test_logic()
