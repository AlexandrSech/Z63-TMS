# import main
# from main import *
# from main import Restaurant, inp

# from main import Restaurant

from time import time
print(time())




exit()



def foo():
    for i in range(10):
        print(i)


class A:
    name: str


class B:
    a: A

    def ret_rest(self):
        return r()



class MyList1:
    value: list
    f: foo

    def __init__(self, *args):
        self.value = list(args)

    def pop(self, _index=0):
        result = self.value[_index]
        del self.value[_index]
        return result


class MyList2:
    value: list

    def myinit(self, *args):
        self.value = list(args)


l1 = MyList1(1,2,3,4,5)
print(l1.pop())
print(l1.pop(-1))

print(l1.value)

l2 = MyList2()
l2.myinit(1,2,3,4,5)
