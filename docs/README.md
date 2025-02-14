# Geometric Library

Geometric Library is a Python library designed to perform geometric calculations. This library provides various functions to calculate areas, perimeters, and volumes of different geometric shapes, including circles, rectangles, and spheres.

## Key Features:
- Calculate area and perimeter for various shapes.
- Efficient algorithms for geometric computations.
- Easy to integrate with other projects.

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Документация функций
## Circle
## Функция area(r)
**Описание**: Вычисляет площадь круга с радиусом r.

**Параметры**:
- r (float): Радиус круга.

**Возвращает**: Площадь круга.

**Пример использования**:
```python
import math
area(5)  # Возвращает 78.54
```

## Функция `perimeter(r)`
Вычисляет периметр круга с радиусом `r`.

- **Параметры**:  
  - `r` (float): радиус круга.
- **Возвращает**:  
  - Периметр круга.

**Пример использования**:
```python
import math
perimeter(5)  # Возвращает 31.42
```

## Square
## Функция area(a)
Вычисляет площадь квадрата со стороной a.

- **Параметры**:  
  - a (float): длина стороны квадрата.
- **Возвращает**:  
  - Площадь квадрата.

**Пример использования**:
```python
import math
area(5)  # Возвращает 25.00
```

## Функция `perimeter(a)`
Вычисляет периметр квадрата со стороной `a`.

- **Параметры**:  
  - `a` (float): длина стороны квадрата.
- **Возвращает**:  
  - Периметр квадрата.

**Пример использования**:
```python
import math
perimeter(5)  # Возвращает 20.00
```

## Triangle
## Функция area(a, b, c)
Вычисляет площадь треугольника по полупериметру со сторонами a, b и c.

- **Параметры**:  
  - a (float): первая сторона треугольника.
  - b (float): вторая сторона треугольника.
  - c (float): третья сторона треугольника.
- **Возвращает**:  
  - Площадь треугольника.

**Пример использования**:
```python
import math
area(5, 5, 5)  # Возвращает 7.50
```

## Функция `perimeter(a, b, c)`
Вычисляет периметр треугольника со сторонами `a`, `b`, `c`.

- **Параметры**:  
  - `a` (float): первая сторона треугольника.
  - `b` (float): вторая сторона треугольника.
  - `c` (float): третья сторона треугольника.
- **Возвращает**:  
  - Периметр треугольника.

**Пример использования**:
```python
import math
perimeter(5)  # Возвращает 15.00
```

