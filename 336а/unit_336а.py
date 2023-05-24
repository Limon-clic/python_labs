from random import random


def mult(start, stop):
    '''перемножение чисел от start до stop'''

    if start > stop:
        raise Exception('start > stop')

    rez = 1
    while start <= stop:
        rez *= start
        start += 1

    return rez


def factotial(start, stop, value):
    '''
    факториал числа, учитывая известный факториал
    value == !start
    '''

    if start > stop:
        raise Exception('start > stop')

    if value == 0:
        value = 1
    return mult(start+1, stop) * value


def logic(n, x):
    '''расчет по формуле'''
    s = 0
    f1 = 0  # значение факториала для 2*i
    f2 = 0  # значение факториала для i**2

    for i in range(1, n+1):
        f1 = factotial(2*(i-1), 2*i, f1)
        f2 = factotial((i-1)**2, i**2, f2)
        s += (f1 + x) / f2
        # print(f'i = {i}; s = {s:.15f}')
    return s  # факториалы


"""
def factotial(x):
	'''факториал числа'''
	if x == 0:
		return 1
	return x*factotial(x-1)


def logic(n, x):
	'''расчет по формуле'''
	s = 0
	for i in range(1, n+1):
		s += (factotial(2*i) + x) / factotial(i**2)
		print(f'i = {i}; s = {s:.15f}')
	return s  # факториалы
"""
