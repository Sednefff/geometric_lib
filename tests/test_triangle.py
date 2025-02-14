import sys
import os
import unittest
from triangle import area, perimeter


sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)


class TestTriangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(3, 4, 5), 6)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_area_invalid(self):
        with self.assertRaises(TypeError):
            area(3, 4, "five")

    def test_perimeter_invalid(self):
        with self.assertRaises(TypeError):
            perimeter(3, 4, "five")

    def test_invalid_size_area(self):
        with self.assertRaises(TypeError):
            area(3, 4)

    def test_invalid_size_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter(3, 4)


if __name__ == '__main__':
    unittest.main()
