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

circle.perimeter(r) # Пермистр(длина окружности) круга с радиусом r
coinEdgeLength = circle.perimeter(0.5) # 3.141592653589

square.area(a) # Площадь квадрата со стороной a
paintingArea = square.area(8) # 64

square.perimeter(a) # Пермистр квадрата со стороной a
windowPerimeter = square.perimeter(20) # 80

square.perimeter(a) # Пермистр квадрата со стороной a
windowPerimeter = square.perimeter(20) # 80
```
### История изменений

    : Добавлена документация
    commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (HEAD -> main, origin/main, origin/HEAD)
    Date: Thu Mar 4 14:55:29 2021 +0300

    : Добавлены реализации компонент круга и квадрата
    commit $ba9aeb3cea847b63a91ac378a2addb75868246o
    Date: Thu Mar 4 14:54:08 2021 +0300