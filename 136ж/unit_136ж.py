from random import random


def print_array(arr):  # вывод массива
    for i in range(len(arr)):
        print(f"{arr[i]:.3f} ", end="")
    print()


def random_array(n):  # создание массива случ. ч. от -50 до 50
    arr = [round(random() * 100 - 50, 3) for i in range(n)]
    return arr  # мин, макс, раунд


def sum_search(arr):  # сумма эл. массива по заданию
    s = 0
    z = 1
    for i in range(len(arr)):
        s += arr[i]*z
        z *= -1
    return s
