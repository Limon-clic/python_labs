import numpy as np

def create_matrix(minn: float, maxx: float, n: int):
    '''создание матрицы n на n, с заданными мин. и макс. значениями'''

    '''...uniform создает n мерный массив используя случайные выборки из равномерного распределения
    здесь мин. , макс. значения в массиве и размер массива'''
    return np.random.uniform(minn, maxx, (n, n))


def print_matrix(matrix, n, floatDigitsAmount: int = 3, numberSymbolsAmount: int = 8):
    '''печать матрицы с зажданным кол-вом знаков после запятой и расстоянием между элементами матрицы'''
    for i in range(0, n):
        for j in range(0, n):
            print(f"{matrix[i][j]:{numberSymbolsAmount}.{floatDigitsAmount}f}", end='')
        print()
        
def flip(matrix, n): # срезы
    '''изменение строк и столбцов местами'''
    temp_matrix = create_matrix(0, 0, n) # промежуточная матрица
    for i in range(0, n):
        for j in range(0, n):
            temp_matrix[i][j] = matrix[j][i]
    return temp_matrix