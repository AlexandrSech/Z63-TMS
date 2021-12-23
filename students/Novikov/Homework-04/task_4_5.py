"""5) Составить список чисел Фибоначчи содержащий 15 элементов.
(Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны либо 1 и 1, а каждое последующее
 число равно сумме двух предыдущих чисел. Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
"""


def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci2(my_new_list, n):
    my_new_list.append(1)
    my_new_list.append(1)
    i = 2
    while i < n:
        my_new_list.append(my_new_list[i - 1] + my_new_list[i - 2])
        i += 1
    return my_new_list


num = 15

i = 0
print("Первая попытка:")
my_list = list()
while i < num:
    my_list.append(fibonacci(i))
    i += 1
print(my_list)

print("Вторая попытка:")
my_list2 = list()
my_list2 = fibonacci2(my_list2, num)
print(my_list2)
