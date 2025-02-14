import math


def areaCircle(r):
    '''
    Принимает переменную r - радиус круга и возвращает значение площади круга.
    По формуле S = pi * r * r находится площадь;
    Пример вызова функции:
    Input: 9
    Output: 254.469
    '''
    if not isinstance(r, (int, float)) or r <= 0:
        raise ValueError("Радиус должен быть положительным!")
    return math.pi * r * r


def perimeterCircle(r):
    '''
    принимает переменную r - радиус круга и возвращает значение периметра круга.
    По формуле S = pi * r * 2 находится длина;
    Пример вызова функции:
    Input: 9
    Output: 56.54867
    '''
    if not isinstance(r, (int, float)) or r <= 0:
        raise ValueError("Радиус должен быть положительным!")
    return 2 * math.pi * r
def areaTriangle(a, h):
    '''
	принимает переменные a - сторона и h - высота и возвращает значение площади.
	По формуле S = a * h / 2 находится площадь
	Пример вызова функции:
    Input: 15 4
    Output: 30
	'''
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, h]):
        raise ValueError("Сторона и высота должны быть положительными!")
	return a * h / 2
def perimeterTriangle(a, b, c):
    '''
    принимает переменные **a**, **b**, **c** - *являющиеся сторонами треугольника* и возвращает значение периметра треугольника.
    По формуле P = a + b + c находится периметр
    Пример вызова функции:
    Input: 5 6 7
    Output: 18
    '''
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
        raise ValueError("Стороны должны быть положительными!")
	return a + b + c

def areaSquare(a):
    '''
    принимает переменную a - сторона квадрата и возвращает значение площади квадрата.
    По формуле S = a * a возвращает площадь.
    Пример вызова функции:
    Input: 8
    Output: 64
    '''
    if not isinstance(a, (int, float)) or a <= 0:
        raise ValueError("Сторона должна быть положительной!")
    return a * a


def perimeterSquare(a):
    '''
    принимает переменную **a** - *сторона квадрата* и возвращает значение периметра квадрата.
    По формуле P = 4 * a возвращает периметр.
    Пример вызова функции:
    Input: 8
    Output: 32
    '''
    if not isinstance(a, (int, float)) or a <= 0:
        raise ValueError("Сторона должна быть положительной!")
    return 4 * a
def areaRectangle(a, b):
    '''
    возвращает значение площади прямоугольника.
    a (int): первая сторона прямоугольника
    b (int): вторая сторона прямоугольника
    По формуле S = a * b возвращает площадь.
    Пример вызова функции:
    Input: 9 13
    Output: 117
    '''
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b]):
        raise ValueError("Стороны должны быть положительными!")
	return a * b
def perimeterRectangle(a, b):
    '''
    принимает переменные a, b - являющиеся различными сторонами прямоугольника и возвращает значение периметра прямоугольника.
    По формуле P = 2 * (a + b) возвращает периметр.
    Пример вызова функции:
    Input: 9 12
    Output: 42
    '''
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b]):
        raise ValueError("Стороны должны быть положительными!")
    return 2 * (a + b)

