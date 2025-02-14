'''
a, b (float):sides of rectangle
return value (float): area of rectangle
'''
def rectangle_area(a: float, b: float) -> float: 
  if a < 0 or b < 0:
    raise ValueError("Invalid side of rectangle")
  return round(a * b, 10)

'''
a, b (float): sides of rectangle
return value (float): perimeter of rectangle
'''
def rectangle_perimeter(a: float, b: float) -> float: 
  if a < 0 or b < 0:
    raise ValueError("Invalid side of rectangle")
  return round(2 * (a + b), 10)