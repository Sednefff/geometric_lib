import math


def area(r):
    ''' Find the area of circle
            Parameters:
                r (double): radius of the circle
            Returned values:
                circle_area (double): area of the circle '''
    return round(round(math.pi, 2) * r * r, 2)


def perimeter(r):
    ''' Find the perimeter of circle
            Parameters:
                r (double): radius of the circle
            Returned values:
                circle_per (double): perimeter of the circle '''
    return round(2 * round(math.pi, 2) * r, 2)

