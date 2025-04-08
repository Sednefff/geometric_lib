from triangle import area, perimeter


def test_area():
    assert area(3, 4, 5) == 6
    assert area(6, 8, 10) == 24


def test_perimeter():
    assert perimeter(3, 4, 5) == 12
    assert perimeter(6, 8, 10) == 24
