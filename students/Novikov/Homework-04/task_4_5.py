"""5) Составить список чисел Фибоначчи содержащий 15 элементов.
(Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны либо 1 и 1, а каждое последующее
 число равно сумме двух предыдущих чисел. Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
"""


def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci2(my_new_list, n):
    my_new_list = [1, 1]
    i = 2
    while i < n:
        my_new_list.append(my_new_list[i - 1] + my_new_list[i - 2])
        i += 1
    return my_new_list


def fibonacci3(my_new_list, n):
    my_new_list = [1, 1]
    for i in range(2, n):
        my_new_list.append(my_new_list[i - 1] + my_new_list[i - 2])
    return my_new_list


num = 15
print("Первая попытка:")
my_list = list()
for i in range(0, num):
    my_list.append(fibonacci(i))
print(my_list)

print("Вторая попытка:")
my_list2 = list()
my_list2 = fibonacci2(my_list2, num)
print(my_list2)

print("Третья попытка:")
my_list3 = list()
my_list3 = fibonacci3(my_list3, num)
print(my_list3)
