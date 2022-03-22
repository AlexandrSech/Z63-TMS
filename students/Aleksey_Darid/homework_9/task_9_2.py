foo = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}
print(foo(a=1, b=2, c=3))