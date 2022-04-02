# 1) Создать матрицу случайных чисел от a до b, размерность матрицы n*m
# 2) Найти максимальный элемент матрицы.
# 3) Найти минимальный минимальный матрицы.
# 4) Найти сумму всех элементов матрицы.
# 5) Найти индекс ряда с максимальной суммой элементов.
# 6) Найти индекс колонки с максимальной суммой элементов.
# 7) Найти индекс ряда с минимальной суммой элементов.
# 8) Найти индекс колонки с минимальной суммой элементов.
# 9) Обнулить все элементы выше главной диагонали.
# 10) Обнулить все элементы ниже главной диагонали.
# 11) Создать две новые матрицы matrix_a, matrix_b случайных чиселразмерностью n*m.
# 12)Создать матрицу равную сумме matrix_a и matrix_b.
# 13)Создать матрицу равную разности matrix_a и matrix_b.
# 14)Создать новую матрицу равную matrix_a умноженной на g. g вводится склавиатура

def matrix_size(): # задаю размерность матрицы сtрок и столбцов
    rows=int(input('Enter number of matrix n*n: '))
    columns=rows
    return rows, columns

def matrix(rows, columns): # генерирую матрицу случайными числами
    import random
    matrix =[]

    for i in range(rows):
        one_str =[] # создаю строку для матрицы
        for j in range(columns):
            one_str.append(random.randint(0, 80))
        matrix.append(one_str) # создаю список списков (матрицу)
    return matrix

def max_number(matrix): # 2 нахожу максимальный элемент матрицы
    max_number = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] > max_number:
                max_number = matrix[i][j]
    return max_number

def min_number (matrix): # 3 нахожу minimal элемент матрицы

    min_number = 1000
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] < min_number:
                min_number = matrix[i][j]
    return min_number

def sum_matrix(matrix): # нахожу сумму матрицы
    sum_matrix = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            sum_matrix += matrix[i][j]
    return sum_matrix

def index_max_sum_row(matrix, columns): # нахожу индекс сторки с минимальной суммой
    index_max_sum_row = 0
    max_sum_row = 0
    sum_row = 0
    for i in range(len(matrix)):
        row = []
    
        for j in range(len(matrix)):
            row.append(matrix[i][j])
        if len(row) == columns:
            sum_row = sum(row)
            if sum_row > max_sum_row:
                max_sum_row =sum_row
                index_max_sum_row = i
    return index_max_sum_row, max_sum_row

def index_min_sum_column(matrix, rows): # нахожу индекс столбца с минимальной суммой
    index_min_sum_column = 0
    min_sum_column = 1000000
    sum_column = 0
    for i in range(len(matrix)):
        column = []
        
        for j in range(len(matrix)):
            column.append(matrix[j][i])
        if len(column) == rows:
            sum_column = sum(column)
            if sum_column < min_sum_column:
                min_sum_column = sum_column
                index_min_sum_column = i
    return index_min_sum_column, min_sum_column



rows, columns = matrix_size()
matrix = matrix(rows, columns)

max_number = max_number(matrix)
min_number = min_number(matrix)
sum_matrix = sum_matrix(matrix)
index_max_sum_row, max_sum_row = index_max_sum_row(matrix, columns)
index_min_sum_column, min_sum_column = index_min_sum_column(matrix, rows)

for q in matrix:
    print(q)

print(f"task 2 max number: {max_number}.")
print(f"task 3 min number: {min_number}.")
print(f"task 4 sum matrix: {sum_matrix}.")
print(f"task 5 index max sum row: {index_max_sum_row} and he = {max_sum_row}.")
print(f"task 6 index min sum column: {index_min_sum_column} and he = {min_sum_column}.")
