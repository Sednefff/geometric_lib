# Geometriclib

## Общее описание
### geometriclib — библиотека для работы с площадью и периметром квадратов и кругов в проектах на python.

## Quick Start

### Клонируйте этот репозиторий в свой проект
```bash
cd project/path/
git clone https://github.com/ваш_username/geometric_lib.git
```
### В любом файле python импортируйте библиотеку
```py
import geometric_lib.circle as circle, geometric_lib.
square as square

print(circle.perimeter(10)) # 62.83185307179586
print(square.area(10)) # 100
```
### Доступные функции и примеры вызова
```py
circle.area(r) # Площадь круга с радиусом r
stadiumArea = circle.area(2) # 12.566370614359

circle.perimeter(r) # Периметр(длина окружности) круга с радиусом r
coinEdgeLength = circle.perimeter(0.5) # 3.141592653589

square.area(a) # Площадь квадрата со стороной a
paintingArea = square.area(8) # 64

square.perimeter(a) # Периметр квадрата со стороной a
windowPerimeter = square.perimeter(20) # 80

square.perimeter(a) # Периметр квадрата со стороной a
windowPerimeter = square.perimeter(20) # 80
```
## История изменения проекта с хешами коммитов

- 96dbea0 добавила файлы библиотеки
- b811f95 добавила файл с общим описанием  
- be216d0 добавила новый файл rectangle.py
- 1078c8d L-03: Docs added
- 8ba9aeb L-03: Circle and square added