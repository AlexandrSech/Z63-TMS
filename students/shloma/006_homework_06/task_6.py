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

# 6.2) Search MAX element:
max_mtx = max(matrix[0])

for i in range(n):
    if max(matrix[i]) > max_mtx:
        max_mtx = max(matrix[i])

print(f"\n2) Максимальный элемент матрицы: {max_mtx}")
# or
# print(f"Максимальный элемент матрицы: {max([max(matrix[i]) for i in range(n)])}")

# 6.3) Search MIN element:
min_mtx = min(matrix[0])

for i in range(n):
    if min(matrix[i]) < max_mtx:
        min_mtx = min(matrix[i])

print(f"3) Минимальный элемент матрицы: {min_mtx}")
# or
# print(f"Минимальный элемент матрицы: {min([min(matrix[i]) for i in range(n)])}")