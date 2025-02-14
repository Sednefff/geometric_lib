import unittest
from triangle import *

class TriangleTestCase(unittest.TestCase):
  def test_one_area(self):
    res = triangle_area(1, 1)
    self.assertEqual(res, 0.5)

  def test_integer_area(self):
    res = triangle_area(673, 8)
    self.assertEqual(res, 2692)
  
  def test_float_area(self):  
    res = triangle_area(983.023, 782.21)
    self.assertEqual(res, 384465.210415)

  def test_negative_first_value_excaption_area(self):
    self.assertRaises(ValueError, triangle_area, -456, 1)

  def test_negative_second_value_excaption_area(self):
    self.assertRaises(ValueError, triangle_area, 823, -1)

  def test_string_argument_area(self):
    self.assertRaises(TypeError, triangle_area, "123")

  def test_one_perimetr(self):
    res = triangle_perimeter(1, 1 ,1)
    self.assertEqual(res, 3)

  def test_integer_perimeter(self):
    res = triangle_perimeter(893, 782, 12345)
    self.assertEqual(res, 14020)
  
  def test_float_perimeter(self):
    res = triangle_perimeter(92440.0133, 123.34, 197)
    self.assertEqual(res, 92760.3533)

  def test_negative_first_value_excaption_perimeter(self):
    self.assertRaises(ValueError, triangle_perimeter, -233, 134, 553)

  def test_negative_second_value_excaption_perimeter(self):
    self.assertRaises(ValueError, triangle_perimeter, 0, -1934, 1234)

  def test_negative_third_value_excaption_perimeter(self):
    self.assertRaises(ValueError, triangle_perimeter, 34, 1134, -973)

  def test_string_argument_perimeter(self):
    self.assertRaises(TypeError, triangle_perimeter, "123")