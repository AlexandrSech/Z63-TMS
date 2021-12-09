def d(x):
    i = 1
    f = 0
    while i <= x:
        f += i
        i += 1
    return f
def r(x):
    i = 1
    f = 1
    while i <= x:
        f *= i
        i += 1
    return f

print(d(7))
print(r(7))
