import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_square_positive_area(self):
        res = area(11)
        self.assertEqual(res, 121)
    
    def test_positive_perimeter(self):
        res = perimeter(11)
        self.assertEqual(res, 44)
    
    def test_zero_side(self):
        res = area(0)
        self.assertEqual(res,0)
        res = perimeter(0)
        self.assertEqual(res,0)
    
    def test_negative_sides(self):
        self.assertRaises(TypeError, area, -1)
        self.assertRaises(TypeError, perimeter, -1)