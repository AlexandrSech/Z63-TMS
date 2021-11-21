from math import fabs

x, y = 3, -5

res = (fabs(x) - fabs(y)) / (1 + fabs(x * y))

print(res)

