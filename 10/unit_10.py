import math

def hight_search(hight):
    '''определяет время падедния объекта на поверхность земли с высоты hight'''
    G = 9.80665
    return math.sqrt(2*hight/G)