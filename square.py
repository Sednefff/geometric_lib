'''
a (float): side of square
return value (float): square area
'''
def square_area(a: float) -> float:
  if a < 0:
    raise ValueError("Invalid side of square")
  return round(a * a, 10)

'''
a (float): side of square
return value (float): perimeter of square
'''
def square_perimeter(a: float) -> float:
  if a < 0:
    raise ValueError("Invalid side of square") 
  return round(4 * a, 10)