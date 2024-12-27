import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_area_with_positive_side(self):
        # Arrange
        side = 4

        # Act
        result = area(side)

        # Assert
        self.assertEqual(result, 16)

    def test_area_with_zero_side(self):
        # Arrange
        side = 0

        # Act
        result = area(side)

        # Assert
        self.assertEqual(result, 0)

    def test_area_with_negative_side_raises_assertion_error(self):
        # Arrange
        side = -2

        # Act & Assert
        with self.assertRaises(AssertionError):
            area(side)

    def test_perimeter_with_positive_side(self):
        # Arrange
        side = 5

        # Act
        result = perimeter(side)

        # Assert
        self.assertEqual(result, 20)

    def test_perimeter_with_negative_side_raises_assertion_error(self):
        # Arrange
        side = -3

        # Act & Assert
        with self.assertRaises(AssertionError):
            perimeter(side)


if __name__ == "__main__":
    unittest.main()
