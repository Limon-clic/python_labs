'''
35 Даны действительные числа x, y, z.
Вычислить:
б) max2(x + y + z/2, xyz) + 1.
'''
__author__ = "Райков"

from unit_35б import *

if __name__ == '__main__':
    x = int(input("введите x\n"))
    y = int(input("введите y\n"))
    z = int(input("введите z\n"))

    ret = summ(x, y, z)
    print(ret[0], ret[1])
    
    answer = sqrt_maxx(ret[0], ret[1]) + 1
    
    print(f"Максимальное значение = {answer:.2f}")
