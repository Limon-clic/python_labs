from random import random


class Class181:

    def __init__(self, n):
        '''конструктор класса
        создает поле - массив случ. цел. чисел размера n
        создает поле n - размер массива'''
        self.n = n
        self.arr = [int(random() * 100 - 50) for i in range(self.n)]
        # print_n()

    def print_n(self):
        print('n = ', self.n)

    def print_arr(self):
        print('arr = ', self.arr)

    def set_arr(self, arr):
        self.arr = arr

    def print_array(self):
        for i in range(self.n):
            print("[", i, "] = ", self.arr[i])

    def logic(self):
        """Получить сумму тех чисел данной последовательности, которые
            а)кратные 5"""
        s = 0
        for i in range(self.n):
            if self.arr[i] % 5 == 0:
                s += self.arr[i]
        return s  # лямбда и параметр
