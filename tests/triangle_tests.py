import unittest
from triangle import area as area_triangle
from triangle import perimeter as perimeter_triangle

class TestTriangleFunctions(unittest.TestCase):

    def test_area_triangle(self):
        # Integer values
        self.assertEqual(area_triangle(0, 5), 0)
        self.assertEqual(area_triangle(1, 1), 0.5)
        self.assertEqual(area_triangle(6, 3), 9)
        self.assertEqual(area_triangle(20, 20), 200)
        self.assertEqual(area_triangle(102, 30), 1530)
        self.assertEqual(area_triangle(1237, 7321), 4528038.5)
        self.assertEqual(area_triangle(210305, 180206), 18949111415)

        # Double values
        self.assertEqual(area_triangle(0.0, 131302.19321922), 0.0)
        self.assertEqual(area_triangle(2.71, 3.14), 4.25)
        self.assertEqual(area_triangle(3.14, 27.38), 42.99)
        self.assertEqual(area_triangle(102.102, 13.132), 670.40)

    def test_perimeter_triangle(self):
        # Integer values
        self.assertEqual(perimeter_triangle(1, 2, 3), 6)
        self.assertEqual(perimeter_triangle(10, 30, 50), 90)
        self.assertEqual(perimeter_triangle(30, 239, 566), 835)
        self.assertEqual(perimeter_triangle(102, 1002, 10002), 11106)
        self.assertEqual(perimeter_triangle(1337, 1337, 1337), 4011)

        # Double values
        self.assertEqual(perimeter_triangle(1.2, 2.3, 3.4), 6.9)
        self.assertEqual(perimeter_triangle(10.19, 19.1, 21.16), 50.45)
        self.assertEqual(perimeter_triangle(1331.1331, 8723.8723, 1923.1923), 11978.20)
        self.assertEqual(perimeter_triangle(12938.10, 13984.20, 1387272.102), 1414194.40)
        self.assertEqual(perimeter_triangle(12498172.1209, 194822.12, 1938472.19488), 14631466.44)

if __name__ == '__main__':
    unittest.main()
