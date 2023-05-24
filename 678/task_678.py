__autor__ = 'Райков'
'''
678 Дана действительная квадратная матрица, порядка n.
Преобразовать матрицу по правилу: строку с номером n сделать столбцом с номером n,
а столбец с номером n сделать строкой с номером n.
'''

from unit_678 import *

if __name__ == '__main__':
    n = int(input("введите n: "))

    matrix = create_matrix(-10, 10, n)

    print(type(matrix), '\n')

    print("изначальная матрица")
    print_matrix(matrix, n)

    # меняем столбцы и строки местами
    matrix = flip(matrix, n)

    print("конечная матрица")
    print_matrix(matrix, n)
