from math import fabs                           # импорт функции модуля

x, y = 1, 2                                     # данные числа
v = (fabs(x) - fabs(y)) / 1 + fabs(x * y)       # формула
print("Результат =", v)                         # вывод результата