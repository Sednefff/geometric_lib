import math


def calculate_area(radius):
    assert radius >= 0
    return math.pi * radius * radius


def calculate_perimeter(radius):
    assert radius >= 0
    return 2 * math.pi * radius
