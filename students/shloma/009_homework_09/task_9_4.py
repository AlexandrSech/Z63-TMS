# Task 9.4
# shlom41k


def my_decorator(my_func):
    def wrapper(*args):
        args = args[::-1]   # Меняем порядок аргументов
        my_func(args)
    return wrapper


@my_decorator
def print_args(*args):
    # Тупо выводим аргументы
    [print(*arg, sep=" ") for arg in args]


# Test
print_args("first", 1, 4, 6, 8, "a", "last")







