"""Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε — вещественные, ε > 0),
находящую приближенное значение функции sin( x ):
sin(x) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
В сумме учитывать все слагаемые, модуль которых больше ε .
С помощью Sin1 найти приближенное значение синуса для данного x при шести данных ε """

from math import sin, pi, factorial


def sin1(x, eps):
    summa = 0
    n = 0
    while True:
        to_add = (-1) ** n * x ** (2 * n + 1) / factorial(2 * n + 1)
        if abs(to_add) < eps:
            return summa
        summa += to_add
        n += 1


eps = 0.1
for _ in range(0, 6):
    print("Разница: ", abs(sin(pi / 4) - sin1(pi / 4, eps)))
    eps /= 10
