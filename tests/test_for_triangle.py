import sys
from triangle import area, perimeter
import pytest
sys.path.append('../')


@pytest.mark.parametrize("given, when, then", [
    ("3, 4, 5", "area({}, {}, {})", "6"),
    ("6, 10, 12", "area({}, {}, {})", "29.9")
])  # проверка на корректные значения
def test_triangle_area(given, when, then):
    # Given: подготовка данных
    a, b, c = [int(i) for i in given.split(', ')]
    # When: выполнение действия
    result = round(eval(when.format(a, b, c)), 1)
    # Then: проверка результата
    assert result == float(then)


@pytest.mark.parametrize("given, when, then", [
    ("3, 4, 5", "perimeter({}, {}, {})", "12"),
    ("6, 10, 12", "perimeter({}, {}, {})", "28")
])  # проверка на корректные значения
def test_triangle_perimiter(given, when, then):
    # Given: подготовка данных
    a, b, c = [int(i) for i in given.split(', ')]
    # When: выполнение действия
    result = round(eval(when.format(a, b, c)), 1)
    # Then: проверка результата
    assert result == float(then)


@pytest.mark.parametrize("given, when, then", [
    ("5, 5, 10", "area({}, {}, {})", "0")])
# некорректное поведение кода, треугольник не существует
def test_triangle_no_area(given, when, then):
    # Given: подготовка данных
    a, b, c = [int(i) for i in given.split(', ')]
    # When: выполнение действия
    result = round(eval(when.format(a, b, c)), 1)
    # Then: проверка результата
    assert result == float(then)


@pytest.mark.parametrize("given, when, then", [
    ("1, 2, 20", "perimeter({}, {}, {})", "23")])
# некорректное поведение кода, треугольник не существует
def test_triangle_no_perimiter(given, when, then):
    # Given: подготовка данных
    a, b, c = [int(i) for i in given.split(', ')]
    # When: выполнение действия
    result = round(eval(when.format(a, b, c)), 1)
    # Then: проверка результата
    assert result == float(then)
