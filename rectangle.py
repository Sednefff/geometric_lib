def area(a, b):
    ''' Find the area of rectangle
            Parameters:
                a (double): first side
                b (double): second side
            Returned values:
                rec_area (double): area of the rectangle '''
    return round(a * b, 2)

def perimeter(a, b):
    ''' Find the perimeter of rectangle
            Parameters:
                a (double): first side
                b (double): second side
            Returned values:
                rec_perimeter (double): perimeter of the rectangle '''
    return round((a + b) * 2, 2)
