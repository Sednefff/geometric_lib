def area(a, h):
    ''' Find the area of triangle
            Parameters:
                a (double): side of triangle
                h (double): height of triangle
            Returned values:
                trian_area (double): area of the triangle '''
    return round(a * h / 2, 2)

def perimeter(a, b, c):
    ''' Find the perimeter of triangle
            Parameters:
                a (double): first side
                b (double): second side
                c (double): third side
            Returned values:
                trian_per (double): petimeter of the triangle '''
    return round(a + b + c, 2)
