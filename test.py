import unittest
import math
from square import *
from rectangle import *
from circle import *
from triangle import *


class CircleTestCase(unittest.TestCase):

    def test_area(self):

        self.assertAlmostEqual(CircleArea(2), math.pi * 2 * 2, places=5) 
        self.assertAlmostEqual(CircleArea(0), "error")
        self.assertAlmostEqual(CircleArea(9223372036854775807), math.pi * 9223372036854775807 ** 2, places=5) 
        self.assertAlmostEqual(CircleArea(-8), "error")

    def test_perimeter(self):

        self.assertAlmostEqual(CirclePerimeter(2), 2 * math.pi * 2, places=5)
        self.assertAlmostEqual(CirclePerimeter(0), "error")  
        self.assertAlmostEqual(CirclePerimeter(9223372036854775807), 2 * math.pi * 9223372036854775807, places=5)
        self.assertAlmostEqual(CirclePerimeter(-6), "error")

class SquareTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(SquareArea(-5), "error")
        self.assertEqual(SquareArea(0), "error")
        self.assertEqual(SquareArea(9223372036854775807), 9223372036854775807**2)
        self.assertEqual(SquareArea(10), 100)

    def test_perimeter(self):
        self.assertEqual(SquarePerimeter(-5), "error")
        self.assertEqual(SquarePerimeter(0), "error")
        self.assertEqual(SquarePerimeter(9223372036854775807), 9223372036854775807*4)
        self.assertEqual(SquarePerimeter(10), 40)


class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(RectangleArea(-2, -6), "error")
        self.assertEqual(RectangleArea(0, 5), "error")
        self.assertEqual(RectangleArea(7, 2), 14)
        self.assertEqual(RectangleArea(9223372036854775807, 9223372036854775807), 9223372036854775807**2)

    def test_perimeter(self):
        self.assertEqual(RectanglePerimeter(-5 , -7), "error")
        self.assertEqual(RectanglePerimeter(0, 5), "error")
        self.assertEqual(RectanglePerimeter(7, 2), 18)
        self.assertEqual(RectanglePerimeter(9223372036854775807, 9223372036854775807), 9223372036854775807*2 + 9223372036854775807*2)
 


class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(TriangleArea(-4, -5), "error")
        self.assertEqual(TriangleArea(3, 6), 9)
        self.assertEqual(TriangleArea(9223372036854775807, 2), 9223372036854775807 * 2 / 2)
        self.assertEqual(TriangleArea(7, 8), 28)

    def test_perimeter(self):
        self.assertEqual(TrianglePerimeter(-4, -5, -6),"error")
        self.assertEqual(TrianglePerimeter(3, 4, 5), 12)
        self.assertEqual(TrianglePerimeter(6, 8, 15), "error")
        self.assertEqual(TrianglePerimeter(9223372036854775807, 9223372036854775807, 9223372036854775807), 9223372036854775807*3)


if __name__ == "__main__":
    unittest.main()
