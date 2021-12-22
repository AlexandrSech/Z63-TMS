# 2021-12-14
# shlom41k
# classwork

import time
import os


def logger(foo):

    def inner(*args, **kwargs):

        template = "{time} {point}: {text}\n"
        file_path = "log_file.log"

        # check file
        if not os.path.exists(file_path):
            with open(file_path, mode="w"):
                pass

        with open(file_path, mode="a") as f:
            f.write(template.format(time=time.strftime('%Y-%m-%d %H:%M:%S'), point="START", text=str(foo)))

        res = foo(*args, **kwargs)

        with open(file_path, mode="a") as f:
            f.write(template.format(time=time.strftime('%Y-%m-%d %H:%M:%S'), point="STOP", text=str(foo)))

        return res

    return inner


@logger
def some_fun():
    for i in range(100):
        pass


@logger
def pows():
    return 2 ** 64


@logger
def bar(x: int, y: int):
    return x ** y


if __name__ == "__main__":
    some_fun()
    print(pows())
    print(bar(2, 10))



