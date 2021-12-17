import time
import os.path
import math


def logger(foo):
    def inside(*args, **kwargs):
        # до и после записать время и текст имени функции
        template = "{time} {point} {text}\n"
        file_path = "lof_file.log"

        # проверяет есть ли файл и если нет то создает
        if not os.path.exists(file_path):
            with open(file_path, "w"):
                pass
        with open(file_path, "a") as f:
            f.write(
                template.format(
                    time=time.strftime("%Y.%m.%d %H:%M:%S"),
                    point="START",
                    text=str(foo)
                )
            )

            result = foo(*args, **kwargs)

            f.write(
                template.format(
                    time=time.strftime("%Y.%m.%d %H:%M:%S"),
                    point="END",
                    text=str(foo)
                )
            )
        return result
    return inside


@logger
def foo():
    print("hello world")
    return math.pi


@logger
def bar(x, y):
    return x**y


if __name__ == '__main__':
    foo()
    print(bar(2, 10))
