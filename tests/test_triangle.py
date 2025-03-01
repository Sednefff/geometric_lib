import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_triangle_positive_area(self):
        res = area(10,11)
        self.assertEqual(res, 55)
    
    def test_positive_perimeter(self):
        res = perimeter(11,12,13)
        self.assertEqual(res, 36)
    def test_negative_sides(self):
        self.assertRaises(TypeError, area, -1,20)
        self.assertRaises(TypeError, perimeter, 3,-20,-1)

    
    