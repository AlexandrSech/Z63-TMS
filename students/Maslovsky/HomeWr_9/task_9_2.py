
f = lambda **kwargs: {key * 2: value * 2 for key, value in kwargs.items()}

print(f(zero=0,one=1,two=2))
