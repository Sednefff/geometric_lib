def area(a, h): 
    """
    Calculates the area of a triangle
    
    Input parameters:
    a (float/int): length of triangle's side
    h (float/int): height of a triangle connected to a-side

    Returns:
    float: area of the triangle
    
    Example:
    area(5,6)
    15
    """
    if (a < 0) or (h < 0): raise TypeError
    return a * h / 2 

def perimeter(a, b, c):
    """
    Calculates the perimeter of a triangle
    
    Input parameters:
    a (float/int): length of triangle's side
    b (float/int): length of triangle's side
    c (float/int): length of triangle's side

    Returns:
    float: perimeter of the triangle
    
    Example:
    perimeter(5,6,7)
    18
    """
    if (a < 0) or (b < 0) or (c < 0): raise TypeError
    return a + b + c 