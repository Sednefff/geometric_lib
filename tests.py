import unittest
from math import pi
import rectangle, circle, triangle, square
'''Each test checks if programm returns right number. It tests for perimetr and area'''

class RectangleTestCase(unittest.TestCase):
    def test_area_zero (self) :
        res = rectangle.area (10 , 0)
        self.assertEqual(res, 0)
    def test_area_int (self) :
        res = rectangle.area (231, 45)
        self.assertEqual(res, 10395)
    def test_area_float (self) :
        res = rectangle.area (3.5,2.5)
        self.assertEqual(res, 8.75)
    def test_area_number (self) :
        res = rectangle.area (10, 4.5)
        self.assertEqual(res, 45)
    def test_per_zero (self) :
        res = rectangle.perimeter (10 , 0)
        self.assertEqual(res, 20)
    def test_per_float (self) :
        res = rectangle.perimeter (4.25, 5.75)
        self.assertEqual(res, 20)
    def test_per_int (self) :
        res = rectangle.perimeter (413, 745)
        self.assertEqual(res, 2316)
    def test_per_number (self) :
        res = rectangle.perimeter (45, 21.3)
        self.assertEqual(res, 132.6)
class CircleTestCase(unittest.TestCase) :
    def test_area_null (self) :
        res = circle.area (0)
        self.assertEqual(res, 0)
    def test_area_int (self) :
        res = circle.area (3)
        self.assertEqual(res, 9 * pi)
    def test_area_float (self) :
        res = circle.area (7.4)
        self.assertEqual(res, 54.76 * pi)
    def test_area_number (self) :
        res = circle.area (812)
        self.assertEqual(res, 659344 * pi)
    def test_per_zero(self):
        res = circle.perimeter (0)
        self.assertEqual(res, 0)
    def test_per_number (self) :
        res = circle.perimeter (9862)
        self.assertEqual(res, 19724 * pi)
    def test_per_float (self) :
        res = circle.perimeter (34.7)
        self.assertEqual(res, 69.4 * pi)
    def test_per_int (self) :
        res = circle.perimeter (8)
        self.assertEqual(res, 16 * pi)

class SquareTestCase(unittest.TestCase) :
    def test_area_zero (self) :
        res = square.area (0)
        self.assertEqual(res, 0)
    def test_area_float(self):
        res = square.area (9.6)
        self.assertEqual(res, 92.16)
    def test_area_number(self):
        res = square.area (941)
        self.assertEqual(res, 885481)
    def test_area_int (self) :
        res = square.area (7)
        self.assertEqual(res, 49)
    def test_per_zero (self) :
        res = square.perimeter (0)
        self.assertEqual(res, 0)
    def test_per_int (self) :
        res = square.perimeter (33)
        self.assertEqual(res, 132)
    def test_per_float (self) :
        res = square.perimeter (9.3)
        self.assertEqual(res, 37.2)
    def test_per_number (self) :
        res = square.perimeter (9879)
        self.assertEqual(res, 39516)
class TriangleTestCase(unittest.TestCase) :
    def test_area_zero (self) :
        res = triangle.area (10 , 0)
        self.assertEqual(res, 0)
    def test_area_number (self) :
        res = triangle.area (3, 23.5)
        self.assertEqual(res, 35.25)
    def test_area_float (self) :
        res = triangle.area (78.25, 25.4)
        self.assertEqual(res, 993.775)
    def test_area_int (self) :
        res = triangle.area (99887, 88556)
        self.assertEqual(res, 4422796586)
    def test_per_zero (self) :
        res = triangle.perimeter (0, 0, 0)
        self.assertEqual(res, 0)
    def test_per_int (self) :
        res = triangle.perimeter (45378, 96343, 76845)
        self.assertEqual(res, 218566)
    def test_per_float (self) :
        res = triangle.perimeter (865.3, 342.8, 498.45)
        self.assertEqual(res, 1706.55)
    def test_per_number (self) :
        res = triangle.perimeter (873, 371.23, 509)
        self.assertEqual(res, 1753.23)


