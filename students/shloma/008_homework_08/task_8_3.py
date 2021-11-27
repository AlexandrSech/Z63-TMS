# Task 8.3
# shlom41k

from math import factorial, pi


def sin1(x, eps):
    sum = 0     # Сумма ряда
    k = x       # Первый член ряда
    n = 0       # Степень

    while abs(k) > eps:
        sum += k
        n += 1
        k = pow(-1, n) * (pow(x, 2 * n + 1) / factorial(2 * n + 1))

    return sum

# Test
print(sin1(pi / 2, 0.001))      # sin(pi/2) = sin(90) = 1               # my_answer = 0.9998431013994987
print(sin1(pi / 4, 0.00001))    # sin(pi/4) = sin(45) = (2^0.5) / 2     # my_answer = 0.7071064695751781
print(sin1(pi / 6, 0.001))      # sin(pi/6) = sin(30) = 0.5             # my_answer = 0.49967417939436376
print(sin1(pi, 0.005), "\n")    # sin(pi) = sin(180) = 0                # my_answer = -0.00044516023820921277

print(sin1(pi / 2, 0.1))        # sin(pi/2) = sin(90) = 1               # my_answer = 0.9248322292886504
print(sin1(pi / 2, 0.01))       # sin(pi/2) = sin(90) = 1               # my_answer = 1.0045248555348174
print(sin1(pi / 2, 0.05))       # sin(pi/2) = sin(90) = 1               # my_answer = 1.0045248555348174
print(sin1(pi / 2, 0.001))      # sin(pi/2) = sin(90) = 1               # my_answer = 0.9998431013994987
print(sin1(pi / 2, 0.002))      # sin(pi/2) = sin(90) = 1               # my_answer = 0.9998431013994987
print(sin1(pi / 2, 0.000001))   # sin(pi/2) = sin(90) = 1               # my_answer = 0.999999943741051
