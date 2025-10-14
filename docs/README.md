# Geometric Lib

## Общее описание решения
Библиотека **Geometric Lib** — это учебный проект на Python для вычисления площадей и периметров простых геометрических фигур.
Реализованы функции для круга, квадрата, прямоугольника и треугольника.

---

##️ Описание функций

### circle.py
- `area(r)` — вычисляет площадь круга  
- `perimeter(r)` — вычисляет длину окружности

### square.py
- `area(a)` — вычисляет площадь квадрата  
- `perimeter(a)` — вычисляет периметр квадрата

### rectangle.py
- `area(a, b)` — вычисляет площадь прямоугольника  
- `perimeter(a, b)` — вычисляет периметр прямоугольника

---

## Примеры вызова

```python
from geometric_lib.square import area, perimeter
print(area(4))      # 16
print(perimeter(4)) # 16

---

## История изменений проекта

* 3c9435f Добавлены docstring-комментарии для функций area() и perimeter() в rectangle.py
* d179239 Добавлены docstring-комментарии для функций area() и perimeter() в square.py
* 32d3baf Добавлены docstring-комментарии для функций area() и perimeter() в circle.py
* d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
* 8ba9aeb L-03: Circle and square added
