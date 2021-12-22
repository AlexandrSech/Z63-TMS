# 2021-12-07
# classwork

import time

from task_5_1 import Restaurant
from time import ctime, time


def foo():
    for i in range(10):
        print(i)
    # return True


class A:
    name: str


class B:
    a: A

    def print_rest(self):
        return Restaurant.describe_restaurant()


class MyList:
    value: list
    f: foo

    def __init__(self, *args):
        self.value = list(args)

    def pop(self, _index=0):
        res = self.value[_index]
        del self.value[_index]
        return res


class MyList2:
    value: list

    def myinit(self, *args):
        self.value = list(args)


if __name__ == "__main__":
    print(ctime())
    print(time())
    print(__name__)
    print(Restaurant.__name__)





