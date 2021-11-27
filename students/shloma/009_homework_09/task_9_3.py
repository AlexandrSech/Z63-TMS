# Task 9.3
# shlom41k


def my_decorator(my_func):
    # print('Входим в декоратор')
    def wrapper(lst):
        # print('Входим в функцию-обёртку')
        # print('Выполняем предварительную фильтрацию данных - удаляем четные элементы')
        [lst.pop(i) for i, v in enumerate(lst) if not v % 2]
        # print('Выполняем обёрнутую функцию...')
        my_func(lst)
        # print('Выходим из обёртки')
    # print('Выходим из декоратора')
    return wrapper


@my_decorator
def print_list(lst: list):
    print(lst)


# Test
l = [1, 2, 3, 4, 5, 6, 7, 8, 10, 13, 15, 20]
print_list(l)







