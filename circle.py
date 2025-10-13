import math


def area(r):
    '''
    Функция area:
    Вычисляет площадь круга
    
    Параметры:
    r (float): радиус круга
    
    Возвращаемое значение:
    float: площадь круга
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Функция perimeter:
    Вычесляет периметр круга 

    Параметр:
    r (float): радиус круга

    Возвращаемое значение:
    float: периметр(длину) круга
    '''
    return 2 * math.pi * r

