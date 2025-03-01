import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_positive_area(self):
        res = area(10,11)
        self.assertEqual(res, 110)
    
    def test_positive_perimeter(self):
        res = perimeter(11, 1)
        self.assertEqual(res, 24)
    
    def test_zero_side(self):
        res = area(0,121321313124143)
        self.assertEqual(res,0)
        res = area(121321313124143,0)
        self.assertEqual(res,0)
    
    def test_negative_sides(self):
        self.assertRaises(TypeError, area, -1,20)
        self.assertRaises(TypeError, perimeter, 20,-1)