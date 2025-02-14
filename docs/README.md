# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2(a + b)
- Square: P = 4a
- Triangle: P = a + b + c


# How the programs works
The project includes 4 files: [circle.py](/circle.py), [rectangle.py](/rectangle.py), [square.py](/square.py) and [triangle.py](/triangle.py). Each of them, when entering a parameter of the corresponding shape (side length or radius), calculates and outputs the area and perimeter of this shape using mathematical formulas.

> *All further formulas used to calculate the area and perimeter can be found in ***Math formulas***.*

## About ***[circle.py](/circle.py)***
```python
import math


def area(r):
    return math.pi * r * r
'''According to the given radius of the circle outputs its area.
        Parameters: 
            r(int or float) - radius of the circle;
            pi - math constant;
        Return value:
            area(r) - area of a circle with this radius. 
'''

def perimeter(r):
    return 2 * math.pi * r
'''According to the given radius of the circle outputs its perimeter.
        Parameters: 
            r(int or float) - radius of the circle;
            pi - math constant;
        Return value:
            perimeter(r) - perimeter of a circle with this radius. 
'''
```
***Launch example:***
```
Radius of the circle: 4
Area: 50.26548245743669 
Perimeter: 25.132741228718345
```
## About ***[rectangle.py](/rectangle.py)***
```python
def area(a, b): 
    return a * b 
'''According to the given lengths of the sides of the rectangle outputs its area.
        Parameters: 
            a(int or float) - the length of the one side of the rectangle;
            b(int or float) - the length of the second side of the rectangle;
        Return value: 
            area(a, b) - area of a rectangle with this sides. 
'''

def perimeter(a, b): 
    return (a + b) * 2 
'''According to the given lengths of the sides of the rectangle outputs its perimeter.
        Parameters: 
            a(int or float) - the length of the one side of the rectangle;
            b(int or float) - the length of the second side of the rectangle;
        Return value: 
            perimeter(a, b) - perimeter of a rectangle with this sides. 
'''
```
***Launch example:***
```
First side of the rectangle: 4
Second side of the rectangle: 9
Area: 36
Perimeter: 26
```
## About ***[square.py](/square.py)***
> *Note that a **square** is a special case of a **rectangle**, that is, to calculate the area and perimeter of a **square**, you can use and **rectangle.py** (a and b will be equal)*
```python
def area(a):
    return a * a

'''According to the given lengths of the side of the square outputs its area.
        Parameters: 
            a(int or float) - the length of the side of the square;
        Return value: 
            area(a) - area of a square with this side. 
'''
def perimeter(a):
    return 4 * a
'''According to the given lengths of the side of the square outputs its perimeter.
        Parameters: 
            a(int or float) - the length of the side of the square;
        Return value: 
            perimeter(a) - perimeter of a square with this side. 
'''
```
***Launch example:***
```
Side of the square: 7
Area: 49
Perimeter: 28
```
## About ***[triangle.py](/triangle.py)***
```python
def area(a, h): 
    return a * h / 2 
'''According to the given lengths of the sides of the triangle outputs its area.
        Parameters: 
            a(int or float) - the length of the one side of the triangle;
            h(int or float) - the length of the height drawn to this side;
        Return value: 
            area(a, h) - area of a triangle with this sides. 
'''
def perimeter(a, b, c): 
    return a + b + c 
'''According to the given lengths of the sides of the triangle outputs its perimeter.
        Parameters: 
            a(int or float) - the length of the one side of the triangle;
            b(int or float) - the length of the second side of the triangle;
            c(int or float) - the length of the third side of the triangle;
        Return value: 
            perimeter(a, b, c) - perimeter of a triangle with this sides. 
'''
```

> *In fact, it is not necessary to know the **height** of the triangle, three of its sides will be enough to calculate the area (according to **[Heron's formula](https://en.wikipedia.org/wiki/Heron%27s_formula)**)*

***Launch example:***
```
First side of the triangle: 4
Second side of the triangle: 5
Third side of the triangle: 6
Height drawn to first side: 4.9607837082461075
Area: 9.921567416492215
Perimeter: 15
```
## Updates:
1) Added function **hypotenuse**, which counts the length of the hypotenuse along two sides of a rectangular triangle.
2) In **[tests.py](/Lab4/tests.py)** created unittests for rectangle's area, triangle's area and hypotenuse.
> *For launch tests write in console* ```python -m unittest tests.py```.
### About **[tests.py](/Lab4/tests.py)**
```python
import unittest
from tabulate import tabulate
'''Previous "from" for tabulate our data'''
def rectangle_area(a, b): 
    return a * b 

def triangle_area(a, h): 
    return a * h / 2 

def hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

class TestCase(unittest.TestCase):
    results = []
    '''This is for create our tab'''
    def add_result(self, test_name, inputs, expected, actual):
        self.results.append([test_name, inputs, expected, actual, "Passed" if expected == actual else "Not passed"])
    '''Tests'''
    def test_zero_area_rect(self):
        inputs = (10000000, 0)'''Input data'''
        expected = 0'''Expected answer'''
        actual = rectangle_area(*inputs)'''Actual answer'''
        self.add_result("test_zero_area_rect", inputs, expected, actual)'''Added our results in tab'''

    def test_square_area_rect(self):
        inputs = (5, 5)
        expected = 25
        actual = rectangle_area(*inputs)
        self.add_result("test_square_area_rect", inputs, expected, actual)

    def test_big_square_area_rect(self):
        inputs = (13428765983984678, 13428765983984678)
        expected = 180331755852623977151186538763684
        actual = rectangle_area(*inputs)
        self.add_result("test_big_square_area_rect", inputs, expected, actual)

    def test_normal_numbers1_area_rect(self):
        inputs = (120, 100)
        expected = 12000
        actual = rectangle_area(*inputs)
        self.add_result("test_normal_numbers1_area_rect", inputs, expected, actual)
    
    def test_normal_numbers2_area_rect(self):
        inputs = (123456, 234567)
        expected = 28958703552
        actual = rectangle_area(*inputs)
        self.add_result("test_normal_numbers2_area_rect", inputs, expected, actual)

    def test_big_numbers_area_rect(self):
        inputs = (340587394587340, 908623498)
        expected = 309465709844655137315320
        actual = rectangle_area(*inputs)
        self.add_result("test_big_numbers_area_rect", inputs, expected, actual)
    
    def test_zero_area_tr(self):
        inputs = (10000000, 0)
        expected = 0.0
        actual = triangle_area(*inputs)
        self.add_result("test_zero_area_tr", inputs, expected, actual)

    def test_normal_numbers1_area_tr(self):
        inputs = (120, 100)
        expected = 6000.0
        actual = triangle_area(*inputs)
        self.add_result("test_normal_numbers1_area_tr", inputs, expected, actual)
    
    def test_normal_numbers2_area_tr(self):
        inputs = (123456, 234567)
        expected = 14479351776.0
        actual = triangle_area(*inputs)
        self.add_result("test_normal_numbers2_area_tr", inputs, expected, actual)

    def test_big_numbers_area_tr(self):
        inputs = (34058739, 908623)
        expected = 15473276803198.5
        actual = triangle_area(*inputs)
        self.add_result("test_big_numbers_area_tr", inputs, expected, actual)

    def test_zero_hyp(self):
        inputs = (10000000, 0)
        expected = 10000000.0
        actual = hypotenuse(*inputs)
        self.add_result("test_zero_hyp", inputs, expected, actual)
    
    def test_normal_numbers1_hyp(self):
        inputs = (120, 160)
        expected = 200.0
        actual = hypotenuse(*inputs)
        self.add_result("test_normal_numbers1_hyp", inputs, expected, actual)

    def test_normal_numbers2_area_tr(self):
        inputs = (12012, 1602)
        expected = 12118.355829071863
        actual = hypotenuse(*inputs)
        self.add_result("test_normal_numbers2_hyp", inputs, expected, actual)

    def test_big_numbers_hyp(self):
        inputs = (34058739, 908623)
        expected = 34070857.01925107
        actual = hypotenuse(*inputs)
        self.add_result("test_big_numbers_hyp", inputs, expected, actual)
    
    @classmethod
    '''Print our tab'''
    def tearDownClass(cls):
        print(tabulate(cls.results, headers=["Test's name", "Input", "Expected answer", "Actual answer", "Status"], tablefmt="grid"))
'''This is for work with "RUN" button'''    
if __name__ == '__main__':
    unittest.main()
```
# Project modification history with commit hashes (except the last commit about this documentary)
```
7ae5609 Added a new feature "hypotenuse" and created unittests in tests.py for some functions
1738904 (origin/new_features_467339) Change some phrases in How the programs works
c65f121 Change parameter ruby to python
f92cef8 Comment about restoring a deleted branch has been deleted
970a962 Delete ruby in LAUNCH EXAMPLES
2622278 Added last 2 commits from 1 lab
409b207 Added project's history in README.md
274c9b9 In the beginning added info about deleted branch
4cfd515 Created documentary in README.md
1b60bf6 Create triangle.py and fix rectangle's perimeter
72c6001 Create rectangle.py
d078c8d (upstream/main, upstream/HEAD, origin/main, main) L-03: Docs added
8ba9aeb L-03: Circle and square added
```