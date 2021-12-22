# 2021-12-21
# rec


def foo(i=0):
    print(i)

    if i > 20:
        return "DNO"
    return foo(i+1)


if __name__ == "__main__":
    print(foo())
