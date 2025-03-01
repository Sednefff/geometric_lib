import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_circle_positive_area(self):
        res = area(10)
        self.assertEqual(res, 100 * math.pi)
    
#    def test_failing_test(self):
#        res = area(10)
#        self.assertEqual(res, 0)
    
    def test_positive_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 10 * math.pi)
    
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res,0)
    
    def test_negative_radius(self):
        self.assertRaises(TypeError, area, -1)
