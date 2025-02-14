import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
  def test_one_area(self):
    res = rectangle_area(1, 1)
    self.assertEqual(res, 1)
  
  def test_integer_area(self):
    res = rectangle_area(25, 69)
    self.assertEqual(res, 1725)

  def test_float_area(self):
    res = rectangle_area(634.97, 692.86)
    self.assertEqual(res, 439945.3142)

  def test_negative_first_value_excaption_area(self):
    self.assertRaises(ValueError, rectangle_area, -456, 0)

  def test_negative_second_value_excaption_area(self):
    self.assertRaises(ValueError, rectangle_area, 456, -1244)

  def test_string_argument_area(self):
    self.assertRaises(TypeError, rectangle_area, "123")

  def test_one_perimeter(self):
    res = rectangle_perimeter(1, 1)
    self.assertEqual(res, 4)
  
  def test_integer_perimeter(self):
    res = rectangle_perimeter(123, 67)
    self.assertEqual(res, 380)

  def test_float_perimeter(self):
    res = rectangle_area(137.23, 93.445)
    self.assertEqual(res, 12823.45735)

  def test_negative_first_value_excaption_perimeter(self):
    self.assertRaises(ValueError, rectangle_perimeter, -233, 134)

  def test_negative_second_value_excaption_perimeter(self):
    self.assertRaises(ValueError, rectangle_perimeter, 0, -1134)

  def test_string_argument_perimeter(self):
    self.assertRaises(TypeError, rectangle_perimeter, "123")