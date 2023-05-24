from random import random

class Class73:

    def is_equals(self, x, y): # проверка равенства двух чисел
        if x == y:
            return True
        else:
            return False
        
    def maxx(self, x, y): # максимум из 2 значений
        if x > y:
            return x
        else:
            return y
        
    def replacement(self, k, l): # замена нужными значениями, по заданию
        if self.is_equals(k, l):
            return [0, 0]
        else:
            k = l = self.maxx(k, l)
            return [k, l]

