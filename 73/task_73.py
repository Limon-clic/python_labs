'''
73 Даны целые числа k, l.
Если числа не равны, то заменить каждое из них одним и тем же числом,
равным большему из исходных, а если равны, то заменить числа нулями.
'''

__author__ = "Райков"

from unit_73 import Class73 as unit

if __name__ == '__main__':
        
    k = int(input("введите k\n"))
    l = int(input("введите l\n"))
    
    u = unit()
    answer = u.replacement(k, l)

    print(f"k = {answer[0]:.2f}")
    print(f"l = {answer[1]:.2f}")
