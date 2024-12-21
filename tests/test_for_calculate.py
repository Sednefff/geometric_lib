import sys
from calculate import calc
import circle
import square
import triangle
import pytest
sys.path.append('../')


@pytest.mark.parametrize("given, when, then", [
    ("'circle', 'area', [5]", "calc({}, {}, {})", "78.54"),
])  # проверка корректных значений
def test_circle_area(given, when, then):
    # Given: подготовка данных
    a, b, c = given.split(', ')
    # When: выполнение действия
    request = when.format(a, b, c)
    print(request)
    result = round(eval(request), 2)
    # Then: проверка результата
    assert result == float(then)


@pytest.mark.parametrize("given, when, then", [
    ("'circle', 'perimeter', [5]", "calc({}, {}, {})", "31.42")
])  # проверка корректных значений
def test_circle_perimeter(given, when, then):
    # Given: подготовка данных
    a, b, c = given.split(', ')
    # When: выполнение действия
    request = when.format(a, b, c)
    print(request)
    result = round(eval(request), 2)
    # Then: проверка результата
    assert result == float(then)


@pytest.mark.parametrize("given, when, then", [
    ("'square', 'area', [12]", "calc({}, {}, {})", "144")
])  # проверка корректных значений
def test_square_area(given, when, then):
    # Given: подготовка данных
    a, b, c = given.split(', ')
    # When: выполнение действия
    request = when.format(a, b, c)
    print(request)
    result = round(eval(request), 2)
    # Then: проверка результата
    assert result == float(then)


@pytest.mark.parametrize("given, when, then", [
    ("'circles', 'area', [5]", "calc({}, {}, {})", "AssertionError"),
    ("'SQUARE', 'perimeter', [5]", "calc({}, {}, {})", "AssertionError"),
])  # проверка некорректных значений
def test_figure_no(given, when, then):
    # Given: подготовка данных
    a, b, c = given.split(', ')
    # When: выполнение действия
    request = when.format(a, b, c)
    with pytest.raises(AssertionError) as info:
        result = eval(request)
        return "Такой функции или имени нет"
