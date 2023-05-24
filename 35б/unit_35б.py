# сумма и произведение по заданию
def summ(x, y, z):
    return [x+y+z/2, x*y*z]

# нахождение максимума из 2 значений, возвр. 2 знач.
def sqrt_maxx(x, y): # квадрат
    if x > y:
        return x**2
    else:
        return y**2