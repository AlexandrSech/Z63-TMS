# 7) Дана целочисленная квадратная матрица. Найти в каждой строке 
# наибольший элемент и поменять его местами с элементом главной диагонали.


def matrix_size(): # задаю размерность матрицы сьорок и столбцов
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


def big_numbers(matrix): 
    max_numbers = [] # находим макс числа в каждой строке
    for i in range(len(matrix)):
        max_number_i=0
        for j in range(len(matrix)):
            if matrix[i][j] > max_number_i:
                max_number_i = matrix[i][j]
        max_numbers.append(max_number_i)
    print(f" all max numbers {max_numbers}")
    return max_numbers

def big_number_new_location(matrix, max_numbers): # нахожу самый большой номер в матрице и меняю его метами
    for r in range(len(matrix)):
        for f in range(len(matrix)):
            if matrix[r][f] == max_numbers[r]:
                matrix[r][f] = matrix[r][r]
                matrix[r][r] = max_numbers[r]
   
    return matrix

rows, columns = matrix_size()
matrix = matrix(rows, columns)

for d in matrix:
    print(d)
max_numbers = big_numbers(matrix)
matrix = big_number_new_location(matrix, max_numbers)

print("modified matrix")
for h in matrix:
    print(h)
