import unittest
import math
from Geometry import *
class TestGeometryFunctions(unittest.TestCase):

    def test_areaCircle(self):
        self.assertAlmostEqual(areaCircle(9), 254.46900494077323, places=5)
        self.assertAlmostEqual(areaCircle(1), math.pi, places=5)


    def test_perimeterCircle(self):
        self.assertAlmostEqual(perimeterCircle(9), 56.548667764616276, places=5)
        self.assertAlmostEqual(perimeterCircle(1), 2 * math.pi, places=5)


    def test_areaTriangle(self):
        self.assertEqual(areaTriangle(15, 4), 30)
        self.assertEqual(areaTriangle(10, 5), 25)


    def test_perimeterTriangle(self):
        self.assertEqual(perimeterTriangle(5, 6, 7), 18)
        self.assertEqual(perimeterTriangle(3, 4, 5), 12)


    def test_areaSquare(self):
        self.assertEqual(areaSquare(8), 64)
        self.assertEqual(areaSquare(1), 1)

    def test_perimeterSquare(self):
        self.assertEqual(perimeterSquare(8), 32)
        self.assertEqual(perimeterSquare(1), 4)

    def test_areaRectangle(self):
        self.assertEqual(areaRectangle(9, 13), 117)
        self.assertEqual(areaRectangle(1, 1), 1)


    def test_perimeterRectangle(self):
        self.assertEqual(perimeterRectangle(9, 12), 42)
        self.assertEqual(perimeterRectangle(1, 1), 4)


    def test_areaCircle_zero(self):
        with self.assertRaises(ValueError):
            areaCircle(0)

    def test_perimeterCircle_zero(self):
        with self.assertRaises(ValueError):
            perimeterCircle(0)

    def test_areaRectangle_zero(self):
        with self.assertRaises(ValueError):
            areaRectangle(0, 10)
            areaRectangle(5, 0)

    def test_perimeterRectangle_zero(self):
        with self.assertRaises(ValueError):
            perimeterRectangle(0, 10)
            perimeterRectangle(10, 0)

    def test_areaTriangle_zero(self):
        with self.assertRaises(ValueError):
            areaTriangle(0, 4)
            areaTriangle(5, 0)

    def test_perimeterTriangle_zero(self):
        with self.assertRaises(ValueError):
            perimeterTriangle(0, 5, 6)
            perimeterTriangle(5, 0, 6)
            perimeterTriangle(6, 6, 0)

    def test_areaSquare_zero(self):
        with self.assertRaises(ValueError):
            areaSquare(0)

    def test_perimeterSquare_zero(self):
        with self.assertRaises(ValueError):
            perimeterSquare(0)

    def test_areaCircle_negative(self):
        with self.assertRaises(ValueError):
            areaCircle(-23)

    def test_areaCircle_string(self):
        with self.assertRaises(ValueError):
            areaCircle("n")

    def test_perimeterCircle_negative(self):
        with self.assertRaises(ValueError):
            perimeterCircle(-23)

    def test_perimeterCircle_string(self):
        with self.assertRaises(ValueError):
            perimeterCircle("v")

    def test_areaRectangle_negative(self):
        with self.assertRaises(ValueError):
            areaRectangle(-5, 28)
            areaRectangle(5, -27)

    def test_areaRectangle_string(self):
        with self.assertRaises(ValueError):
            areaRectangle("n", 66)
            areaRectangle(52, "a")

    def test_perimeterRectangle_negative(self):
        with self.assertRaises(ValueError):
            perimeterRectangle(-52, 1)
            perimeterRectangle(1, -56)

    def test_areaTriangle_negative(self):
        with self.assertRaises(ValueError):
            areaTriangle(52, -18)
            areaTriangle(-18, 5)

    def test_perimeterTriangle_negative(self):
        with self.assertRaises(ValueError):
            perimeterTriangle(5, -1000, 6)
            perimeterTriangle(-7, 6, 5)
            perimeterTriangle(5, 6, -9)

    def test_perimeterTriangle_string(self):
        with self.assertRaises(ValueError):
            perimeterTriangle("c", -8, 9)
            perimeterTriangle(-7, "p", 90)
            perimeterTriangle(9, 65, "p")

    def test_areaSquare_negative(self):
        with self.assertRaises(ValueError):
            areaSquare(-52)





if __name__ == '__main__':
    unittest.main()
