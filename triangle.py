def area(a, b, c):  # Площадь указана некорректно
    # Замена на  формулу Герона
    # return (a + b + c) / 2
    p = (a + b + c) / 2
    S = p * (p - a) * (p - b) * (p - c)
    return S ** 0.5


def perimeter(a, b, c):
    return a + b + c
