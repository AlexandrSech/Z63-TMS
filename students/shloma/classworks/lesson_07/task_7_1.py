# 2021-12-14
# shlom41k
# classwork

def deco1(starter):
    print("Decorator started")

    def inner():
        print("Inner started")
        return starter()

    print("Decorator finished")
    return inner


@deco1
def foo():
    print("Hello, world")


@deco1
def foo2():
    return 2 ** 16


if __name__ == "__main__":
    foo()

    print(foo2())
