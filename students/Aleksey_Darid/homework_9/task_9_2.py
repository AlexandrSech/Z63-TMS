foo = lambda **kwargs: str(kwargs.keys()) * 2
slov = {"a":1, "b":2, "c":3, "d":4}
print(foo(slov))