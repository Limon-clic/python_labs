import pytest
from unit_73 import Class73 as unit

def test_is_equals():
    u = unit()
    res = u.is_equals(-1, -1)
    assert res == True # ошибка в test_is_equals(-1, -1)
    
    res1 = u.is_equals(1, 1)
    assert res1 == True # ошибка в test_is_equals(1, 1)
    
    res1 = u.is_equals(1, -1)
    assert res1 == False # ошибка в test_is_equals(1, -1)
    
    res1 = u.is_equals(-1, 1)
    assert res1 == False # ошибка в test_is_equals(-1, 1)
    
def test_maxx():
    u = unit()
    assert u.maxx(1,2) == 2 # ошибка в test_maxx(1,2)
    assert u.maxx(-2,4) == 4 # ошибка в test_maxx(-2,4)
    assert u.maxx(-1,-2) == -1 # ошибка в test_maxx(-1,-2)
    
test_is_equals()
test_maxx()
