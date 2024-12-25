import unittest
import math
from square import *
from rectangle import *
from circle import *
from triangle import *


class CircleTestCase(unittest.TestCase):

    def test_area_positive_radius(self):
        self.assertAlmostEqual(CircleArea(2), math.pi * 2 * 2, places=5)

    def test_area_zero_radius(self):
        self.assertAlmostEqual(CircleArea(0), "error")

    def test_area_large_radius(self):
        self.assertAlmostEqual(CircleArea(9223372036854775807), math.pi * 9223372036854775807 ** 2, places=5)

    def test_area_negative_radius(self):
        self.assertAlmostEqual(CircleArea(-8), "error")

    def test_perimeter_positive_radius(self):
        self.assertAlmostEqual(CirclePerimeter(2), 2 * math.pi * 2, places=5)

    def test_perimeter_zero_radius(self):
        self.assertAlmostEqual(CirclePerimeter(0), "error")

    def test_perimeter_large_radius(self):
        self.assertAlmostEqual(CirclePerimeter(9223372036854775807), 2 * math.pi * 9223372036854775807, places=5)

    def test_perimeter_negative_radius(self):
        self.assertAlmostEqual(CirclePerimeter(-6), "error")


class SquareTestCase(unittest.TestCase):

    def test_area_negative_side(self):
        self.assertEqual(SquareArea(-5), "error")

    def test_area_zero_side(self):
        self.assertEqual(SquareArea(0), "error")

    def test_area_large_side(self):
        self.assertEqual(SquareArea(9223372036854775807), 9223372036854775807 ** 2)

    def test_area_positive_side(self):
        self.assertEqual(SquareArea(10), 100)

    def test_perimeter_negative_side(self):
        self.assertEqual(SquarePerimeter(-5), "error")

    def test_perimeter_zero_side(self):
        self.assertEqual(SquarePerimeter(0), "error")

    def test_perimeter_large_side(self):
        self.assertEqual(SquarePerimeter(9223372036854775807), 9223372036854775807 * 4)

    def test_perimeter_positive_side(self):
        self.assertEqual(SquarePerimeter(10), 40)


class RectangleTestCase(unittest.TestCase):

    def test_area_negative_sides(self):
        self.assertEqual(RectangleArea(-2, -6), "error")

    def test_area_zero_and_positive_sides(self):
        self.assertEqual(RectangleArea(0, 5), "error")

    def test_area_positive_sides(self):
        self.assertEqual(RectangleArea(7, 2), 14)

    def test_area_large_sides(self):
        self.assertEqual(RectangleArea(9223372036854775807, 9223372036854775807), 9223372036854775807 ** 2)

    def test_perimeter_negative_sides(self):
        self.assertEqual(RectanglePerimeter(-5, -7), "error")

    def test_perimeter_zero_and_positive_sides(self):
        self.assertEqual(RectanglePerimeter(0, 5), "error")

    def test_perimeter_positive_sides(self):
        self.assertEqual(RectanglePerimeter(7, 2), 18)

    def test_perimeter_large_sides(self):
        self.assertEqual(RectanglePerimeter(9223372036854775807, 9223372036854775807), 9223372036854775807 * 2 + 9223372036854775807 * 2)


class TriangleTestCase(unittest.TestCase):

    def test_area_negative_sides(self):
        self.assertEqual(TriangleArea(-4, -5), "error")

    def test_area_valid_triangle(self):
        self.assertEqual(TriangleArea(3, 6), 9)

    def test_area_large_sides(self):
        self.assertEqual(TriangleArea(9223372036854775807, 2), 9223372036854775807 * 2 / 2)

    def test_area_positive_sides(self):
        self.assertEqual(TriangleArea(7, 8), 28)

    def test_perimeter_negative_sides(self):
        self.assertEqual(TrianglePerimeter(-4, -5, -6), "error")

    def test_perimeter_valid_triangle(self):
        self.assertEqual(TrianglePerimeter(3, 4, 5), 12)

    def test_perimeter_invalid_triangle(self):
        self.assertEqual(TrianglePerimeter(6, 8, 15), "error")

    def test_perimeter_large_sides(self):
        self.assertEqual(TrianglePerimeter(9223372036854775807, 9223372036854775807, 9223372036854775807), 9223372036854775807 * 3)


if __name__ == "__main__":
    unittest.main()