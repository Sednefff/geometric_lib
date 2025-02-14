import circle
import square
import triangle

figures = ["circle", "square", "triangle"]
functions = ["perimeter", "area"]
required_sizes = {"circle": 1, "square": 1, "triangle": 3}


def calculate(figure, function, size):
    assert figure in figures, f"Invalid figure: {figure}"
    assert function in functions, f"Invalid function: {function}"

    result = eval(f"{figure}.{function}(*{size})")
    print(f"{function.capitalize()} of {figure} is {result}")


if __name__ == "__main__":
    selected_figure = ""
    selected_function = ""
    sizes = []

    while selected_figure not in figures:
        selected_figure = (
            input(f"name: {figures}):\n").strip().lower()
        )

    while selected_function not in functions:
        selected_function = (
            input(f"name: {functions}):\n").strip().lower()
        )

    required_size_count = required_sizes[selected_figure]
    while len(sizes) != required_size_count:
        try:
            sizes = list(
                map(
                    float,
                    input(
                        f"{required_size_count} {selected_figure}:\n"
                    ).split(),
                )
            )
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    calculate(selected_figure, selected_function, sizes)
