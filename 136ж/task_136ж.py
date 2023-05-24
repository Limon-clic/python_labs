__autor__ = 'Райков'

'''
136 Даны натуральное число n, действительные числа a1,..., an. Вычислить:
ж) a1 - a2 + a3 - ... + (-1)*n + 1*an;
'''

from unit_136ж import *

if __name__ == '__main__':
    print("введите n")
    n = int(input())

    arr = random_array(n)
    # исходный массив
    print_array(arr)

    print(f"сумма = {sum_search(arr):.3f}")
