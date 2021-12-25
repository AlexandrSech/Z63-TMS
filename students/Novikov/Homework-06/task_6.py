import random

a = 0
b = 20


def make_matrix(n, m):
    matrix = list()
    for _ in range(n):
        matrix.append([random.randint(a, b) for _ in range(m)])
    return matrix


def print_matrix(matrix):
    for line in matrix:
        print(*line, sep="\t\t")


n = 4
m = 5

# 1) Создать матрицу случайных чисел от a до b, размерность матрицы n*m
matrix = make_matrix(n, m)

print(matrix)
print("Исходная матрица: ")
print_matrix(matrix)

# 2) Найти максимальный элемент матрицы.
maximums = list()
for line in matrix:
    maximums.append(max(line))
print(f"Максимальный элемент матрицы: {max(maximums)}")

# 3) Найти минимальный элемент матрицы.
minimums = list()
for line in matrix:
    minimums.append(min(line))
print(f"Минимальный элемент матрицы: {min(minimums)}")

# 4) Найти сумму всех элементов матрицы.
summ = list()
for line in matrix:
    summ.append(sum(line))
print("Сумма по рядам:", summ)
print(f"Сумма элементов матрицы: {sum(summ)}")

# 5) Найти индекс ряда с максимальной суммой элементов.
maximum = max(summ)
for index, el in enumerate(summ):
    if el == maximum:
        print(f"{index} ряд с максимальной суммой элементов")

# 6) Найти индекс колонки с максимальной суммой элементов.
matrix2 = list()
for j in range(0, m):
    matrix2.append([matrix[i][j] for i in range(0, n)])

print("Новая матрица: ")
print_matrix(matrix2)

summ2 = list()
for line in matrix2:
    summ2.append(sum(line))
print("Сумма по колонкам:", summ2)

maximum = max(summ2)
for index, el in enumerate(summ2):
    if el == maximum:
        print(f"{index} колонка с максимальной суммой элементов")

# 7) Найти индекс ряда с минимальной суммой элементов.
minimum = min(summ)
for index, el in enumerate(summ):
    if el == minimum:
        print(f"{index} ряд с минимальной суммой элементов")

# 8) Найти индекс колонки с минимальной суммой элементов.
minimum = min(summ2)
for index, el in enumerate(summ2):
    if el == maximum:
        print(f"{index} колонка с минимальной суммой элементов")

# 9) Обнулить все элементы выше главной диагонали.
for i in range(0, n):
    for j in range(0, m):
        if j > i:
            matrix[i][j] = 0
print("Обнулили все элементы выше главной диагонали")
print_matrix(matrix)

# 10) Обнулить все элементы ниже главной диагонали.
for i in range(0, n):
    for j in range(0, m):
        if i > j:
            matrix[i][j] = 0
print("Обнулили все элементы ниже главной диагонали")
print_matrix(matrix)

# 11) Создать две новые матрицы matrix_a, matrix_b случайных чисел
# размерностью n*m.
matrix_a = make_matrix(n, m)
matrix_b = make_matrix(n, m)
print("Матрица А: ")
print_matrix(matrix_a)
print("Матрица B: ")
print_matrix(matrix_b)

# 12)Создать матрицу равную сумме matrix_a и matrix_b.
matrix_c = list()
for i in range(0, n):
    matrix_c.append([matrix_a[i][j] + matrix_b[i][j] for j in range(0, m)])
print("Матрица C: ")
print_matrix(matrix_c)

# 13)Создать матрицу равную разности matrix_a и matrix_b.
matrix_d = list()
for i in range(0, n):
    matrix_d.append([matrix_a[i][j] - matrix_b[i][j] for j in range(0, m)])
print("Матрица D: ")
print_matrix(matrix_d)

# 14)Создать новую матрицу равную matrix_a умноженной на g. g вводится с
# клавиатура"""
g = float(input("Введите g: "))
matrix_e = list()
for i in range(0, n):
    matrix_e.append([matrix_a[i][j] * g for j in range(0, m)])
print("Матрица D: ")
print_matrix(matrix_e)

