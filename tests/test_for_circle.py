import sys
from circle import area, perimeter
import pytest
sys.path.append('../')


@pytest.mark.parametrize("given, when, then", [
    ("3", "area({})", "28.3"),
    ("5", "area({})", "78.5")
])
def test_circle_area(given, when, then):
    # Given: подготовка данных
    a = int(given)
    # When: выполнение действия
    result = round(eval(when.format(a)), 1)
    # Then: проверка результата
    assert result == float(then)


@pytest.mark.parametrize("given, when, then", [
    ("4", "perimeter({})", "25.1"),
    ("6", "perimeter({})", "37.7")
])
def test_circle_perimeter(given, when, then):
    # Given: подготовка данных
    a = int(given)
    # When: выполнение действия
    result = round(eval(when.format(a)), 1)
    # Then: проверка результата
    assert result == float(then)