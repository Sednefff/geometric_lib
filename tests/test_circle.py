import unittest
from circle import area, perimeter


class TestCircle(unittest.TestCase):
    def test_area_with_positive_radius(self):
        # Arrange
        radius = 3

        # Act
        result = area(radius)

        # Assert
        self.assertAlmostEqual(result, 28.274333882308138, places=5)

    def test_area_with_zero_radius(self):
        # Arrange
        radius = 0

        # Act
        result = area(radius)

        # Assert
        self.assertEqual(result, 0)

    def test_area_with_negative_radius_raises_assertion_error(self):
        # Arrange
        radius = -1

        # Act & Assert
        with self.assertRaises(AssertionError):
            area(radius)

    def test_perimeter_with_positive_radius(self):
        # Arrange
        radius = 3

        # Act
        result = perimeter(radius)

        # Assert
        self.assertAlmostEqual(result, 18.84955592153876, places=5)

    def test_perimeter_with_negative_radius_raises_assertion_error(self):
        # Arrange
        radius = -1

        # Act & Assert
        with self.assertRaises(AssertionError):
            perimeter(radius)


if __name__ == "__main__":
    unittest.main()
