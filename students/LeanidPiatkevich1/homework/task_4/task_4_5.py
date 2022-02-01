# Task 4.5

''' Составить список чисел Фибоначчи содержащий 15 элементов.
(Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны
либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... ) '''

fibon_number_list = [1, 1]

for i in range(13):
    fibon_number_list.append(fibon_number_list[-2] + fibon_number_list[-1])

print("через for", fibon_number_list)


while len(fibon_number_list) < 15:
    fibon_number_list.append(fibon_number_list[-2] + fibon_number_list[-1])

print("через while", fibon_number_list)
