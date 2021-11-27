# Task 9.2
# shlom41k

f = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}

# Test
print(f(one=1, two=2, three=3))
print(f(x="a", y="b"))
print(f(abc=5, xyz=4, ijk=1, lmn=10))