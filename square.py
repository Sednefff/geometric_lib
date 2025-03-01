
def area(a):
    """
    Calculates the area of a square
    
    Input parameters:
    a (float/int): length of square's side

    Returns:
    float: area of the square
    
    Example:
    area(5)
    25
    """
    if a < 0: raise TypeError
    return a * a


def perimeter(a):
    """
    Calculates the perimeter of a square
    
    Input parameters:
    a (float/int): length of square's side

    Returns:
    float: perimeter of the square
    
    Example:
    perimeter(5)
    20
    """
    if a < 0: raise TypeError
    return 4 * a
