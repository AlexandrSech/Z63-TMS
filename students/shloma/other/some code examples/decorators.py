
def decorate(func):
    def wrapper(value):
        print("Wrapper")
        func(value)
    return wrapper



@decorate
def test(val: int) -> None:
    print(f"Test, value: {val}")

# test = decorate(test)     # Аналогично записи выше
# оборачиваем функцию


test("value in test")