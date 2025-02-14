# Калькулятор геометрических фигур
В репозитории доступны файлы с функциями для вычисления площади и периметра некоторых геометрических фигур (Доступны круг, квадрат, треугольник и прямоугольник). В Calculate.py доступен ввод пользователем с клавиатуры необходимой фигуры, а также её размеров
## Использование calculate.py
1. Запустите программу "calculate.py".
2. Введите название фигуры. Доступные фигуры: Circle (круг), Square (квадрат).
3. Введите название функции: Area (площадь) или Perimeter (периметр).
4. Введите размеры фигуры. Радиус для круга, одну сторону для квадрата.
5. Программа выведет результат.

Описание кода **сalculate.py**

Функция `def calc(fig, func, size)`. Принимает на вход название фигуры, название функции и размер, возвращает результат в зависимости от введённых данных.
Пример использования:
```
Enter figure name, avaliable are 'circle', 'square'
square
Enter function name, avaliable are 'perimeter', 'area'
area
Input figure sizes separated by space, 1 for circle and square
5
25
```
Полное описание кода **calculate.py**: 

`import circle`  Импортируем модуль circle, содержащий функции для работы с окружностями
`import square`  " Импортируем модуль square, содержащий функции для работы с квадратами 

Список доступных фигур
`figs = ['circle', 'square']`
Список доступных функций
`funcs = ['perimeter', 'area']`
Словарь для хранения размеров фигур и соответствующего количества аргументов
`sizes = {}`

Функция для вычисления периметра или площади фигуры
`def calc(fig, func, size):`
    `assert fig in figs`  Проверяем, что фигура допустима 
    `assert func in funcs`  Проверяем, что функция допустима 

Вычисляем результат, вызывая соответствующую функцию из модуля фигуры
`result = eval(f'{fig}.{func}(*{size})')`
Печатаем результат вычисления
`print(f'{func} of {fig} is {result}')`

Основной блок программы 
`if __name__ == "__main__":`
    `func = ''`  Инициализация переменной для функции 
    `fig = ''`   Инициализация переменной для фигуры 
    `size = list()`  Инициализация списка для размеров
    
Цикл для ввода допустимой фигуры 
`while fig not in figs:`
    `fig = input(f"Enter figure name, avaliable are {figs}:\n")` Запрашиваем у пользователя фигуру

Цикл для ввода допустимой функции
`while func not in funcs:`
    `func = input(f"Enter function name, avaliable are {funcs}:\n")`  Запрашиваем у пользователя функцию

Цикл для ввода размеров фигуры 
`while len(size) != sizes.get(f"{func}-{fig}", 1):`
    Запрашиваем размеры, разделенные пробелами
    `size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n")` `split(' ')))`
    
Вызываем функцию calc с введенными параметрами 
`calc(fig, func, size)`

В функциях файлов **triangle.py**, **ractangle.py**, **square.py**, **circle.py** использованы следующие математические формулы:
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

Список последних коммитов с описанием изменений: 
------------------------------------------
b5b0fae L-04: Update docs for calculate.py
d76db2a L-04: Add calculate.py
51c40eb L-04: Doc updated for triangle
d080c78 L-04: Triangle added
d078c8d L-03: Docs added
8ba9aeb L-03: Circle and square added
---------------------------------
