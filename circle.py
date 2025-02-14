import math


def calculate_area(r):
    assert r >= 0
    return math.pi * r * r


def calculate_perimeter(r):
    assert r >= 0
    return 2 * math.pi * r
