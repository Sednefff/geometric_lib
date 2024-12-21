import sys
from square import area, perimeter
import pytest
sys.path.append('../')


@pytest.mark.parametrize("given, when, then", [
    ("3", "area({})", "9"),
    ("5", "area({})", "25"),
])
def test_square_area(given, when, then):
    # Given: подготовка данных
    a = int(given)
    # When: выполнение действия
    result = round(eval(when.format(a)), 1)
    # Then: проверка результата
    assert result == float(then)


@pytest.mark.parametrize("given, when, then", [
    ("4", "perimeter({})", "16"),
    ("6", "perimeter({})", "24")
])
def test_square_perimeter(given, when, then):
    # Given: подготовка данных
    a = int(given)
    # When: выполнение действия
    result = round(eval(when.format(a)), 1)
    # Then: проверка результата
    assert result == float(then)