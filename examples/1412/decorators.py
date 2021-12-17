def deco1(starter):
    def inner():
        print(3)
        temp = starter()
        print(4)
        return temp
    return inner


@deco1
def foo():
    print("hello world")


@deco1
def foo2():
    return 2**16


if __name__ == '__main__':
    # foo()
    print(foo2())
