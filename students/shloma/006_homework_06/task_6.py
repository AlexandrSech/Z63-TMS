# Task 6

from random import randint

# Get input data
# Matrix elements range
a = int(input("Введите нижнюю границу [a]: "))
b = int(input("Введите верхнюю границу [b]: "))

# Matrix size [n x m]
n = int(input("Введите количество строк матрицы [n]: "))
m = int(input("Введите количество столбцов матрицы [m]: "))

# a, b = -10, 10
# n, m, = 4, 4

matrix = list()     # Matrix

# 6.1) Generate matrix elements
for _ in range(n):
    matrix.append([randint(a, b) for _ in range(m)])

# Print matrix
print("\n1) Исходная матрица:")
[print(*matrix[i], sep="\t\t", end="\n") for i in range(n)]