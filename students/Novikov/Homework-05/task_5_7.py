"""7) Дана целочисленная квадратная матрица. Найти в каждой строке наибольший элемент
и поменять его местами с элементом главной диагонали. """

from random import randint

n = 5
matrix = list()
for _ in range(n):
    matrix.append([randint(-10, 10) for _ in range(n)])

print("Исходная матрица: ")
for line in matrix:
    print(*line, sep="\t\t")

for i in range(len(matrix)):
    matrix[i][i] = max(matrix[i])

print("Полученная матрица: ")
for line in matrix:
    print(*line, sep="\t\t")
