import math

'''
r (float): radius of circle
return value (float): area of circle
'''
def circle_area(r: float) -> float:
  if r < 0:
    raise ValueError("Invalid radius of circle")
  return round(math.pi * r * r, 10)

'''
r (float): radius of circle
return value (float): perimeter of circle
'''
def circle_perimeter(r: float) -> float:
  if r < 0:
    raise ValueError("Invalid radius of circle")
  return round(2 * math.pi * r, 10)
