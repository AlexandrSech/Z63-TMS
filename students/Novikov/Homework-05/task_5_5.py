"""5) В массиве целых чисел с количеством элементов 19 определить максимальное число и
заменить им все четные по значению элементы."""

import random

my_list = list()
for _ in range(0, 19):
    my_list.append(random.randint(10, 100))
print(my_list)

max = my_list[0]
counter = 1
while counter < len(my_list):
    if max < my_list[counter]:
        max = my_list[counter]
    counter += 1

i = 0
while i < len(my_list):
    if my_list[i] % 2 == 0:
        my_list[i] = max
    i += 1

print(my_list)
