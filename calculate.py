import circle
import square
import triangle  # Импорт модуля треугольника

# Список доступных фигур
figs = ['circle', 'square', 'triangle']

# Список доступных функций для расчета
funcs = ['perimeter', 'area']

# Словарь для хранения размеров фигур
sizes = {
    'circle': 1,
    'square': 1,
    'triangle': 3
}

# Mapping figure names to their respective modules
fig_modules = {
    'circle': circle,
    'square': square,
    'triangle': triangle
}


def calc(fig: str, func: str, size: list) -> float:
    """
    Вычисляет и выводит результат для заданной фигуры и функции.

    Параметры:
    fig (str): название фигуры ().
    func (str): название функции для расчета ().
    size (list): список параметров фигуры ().

    Возвращаемое значение:
    float: результат расчета.

    Пример вызова:
    calc('circle', 'area', [5])
    """
    if fig not in figs:
        raise ValueError("Некорректная фигура")
    if func not in funcs:
        raise ValueError("Некорректная функция")

    module = fig_modules[fig]
    func_to_call = getattr(module, func)
    result = func_to_call(*size)
    print(f'{func} of {fig} is {result}')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    # Запрос имени фигуры у пользователя
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    # Запрос имени функции у пользователя
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    # Запрос параметров фигуры у пользователя
    while len(size) != sizes.get(fig, 1):
        try:
            size = list(
                map(
                    int,
                    input(
                        "Input figure sizes separated by space\n"
                    ).split()
                )
            )
        except ValueError:
            print("Please enter valid integer values.")

    # Вызов функции для расчета и вывода результата
    calc(fig, func, size)
