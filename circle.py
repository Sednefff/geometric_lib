import math


def area(r):
    """
    Calculates the area of a circle
    
    Input parameters:
    r (float/int): radius of a circle

    Returns:
    float: area of the circle
    
    Example:
    area(5)
    78.53981633974483
    """
    if r < 0: raise TypeError
    return math.pi * r * r


def perimeter(r):
    """
    Calculates the perimeter of a circle
    
    Input parameters:
    r (float/int): radius of a circle

    Returns:
    float: perimeter of the circle
    
    Example:
    perimeter(5)
    31.41592653589793
    """
    if r < 0: raise TypeError
    return 2 * math.pi * r

