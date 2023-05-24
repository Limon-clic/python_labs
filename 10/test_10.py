import pytest
from unit_10 import *

def test_hight_search():
    res = hight_search(5)
    # при проверке учитываем погрешность мз за округления
    assert res-1.0098 <= 0.01 # ошибка в test_hight_search
    
test_hight_search()