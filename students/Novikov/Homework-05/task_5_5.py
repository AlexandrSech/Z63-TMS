"""5) В массиве целых чисел с количеством элементов 19 определить максимальное число и
заменить им все четные по значению элементы."""

from random import randint

my_list = list()
for _ in range(20):
    my_list.append(randint(0, 100))
print(my_list)

maxim = max(my_list)

for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0:
        my_list[i] = maxim
print(my_list)
