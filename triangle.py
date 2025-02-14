'''
a (float): base side of triangle
h (float): height of triangle
return value (float): area of triangle
'''
def triangle_area(a: float, h: float) -> float:
  if a < 0:
    raise ValueError("Invalid side of triangle")
  if h < 0:
    raise ValueError("Invalid height of triangle")
  return round(a * h / 2, 10)

'''
a, b, c (float): is a sides of triangle
return value (float): perimeter of triangle
'''
def triangle_perimeter(a: float, b: float, c: float) -> float:    
  if a < 0 or b < 0 or c < 0:
    raise ValueError("Invalid side of triangle")
  return round(a + b + c, 10)