def area(a, b):
    """
    Calculates the area of a rectangle
    
    Input parameters:
    a (float/int): height of a rectangle
    b (float/int): width of a rectangle

    Returns:
    float: area of the rectangle
    
    Example:
    area(5,6)
    30
    """
    if a < 0 or b < 0: raise TypeError
    return a * b 

def perimeter(a, b): 
    """
    Calculates the perimeter of a rectangle
    
    Input parameters:
    a (float/int): height of a rectangle
    b (float/int): width of a rectangle

    Returns:
    float: perimeter of the rectangle
    
    Example:
    perimeter(5,6)
    22
    """
    if a < 0 or b < 0: raise TypeError
    return (a + b)*2