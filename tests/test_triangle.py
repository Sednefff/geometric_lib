import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_area_with_valid_sides(self):
        # Arrange
        a, b, c = 3, 4, 5

        # Act
        result = area(a, b, c)

        # Assert
        self.assertAlmostEqual(result, 6.0, places=5)

    def test_area_with_negative_sides_raises_assertion_error(self):
        # Arrange
        invalid_sides = [(-1, 2, 3), (1, -2, 3), (1, 2, -3)]

        for sides in invalid_sides:
            with self.assertRaises(AssertionError):
                area(*sides)

    def test_perimeter_with_valid_sides(self):
        # Arrange
        a, b, c = 3, 4, 5

        # Act
        result = perimeter(a, b, c)

        # Assert
        self.assertEqual(result, 12)

    def test_perimeter_with_negative_sides_raises_assertion_error(self):
        # Arrange
        a, b, c = -1, 4, 5

        # Act & Assert
        with self.assertRaises(AssertionError):
            perimeter(a, b, c)


if __name__ == "__main__":
    unittest.main()
