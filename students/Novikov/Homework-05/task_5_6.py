"""6) Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число больше предыдущего)."""

import random

my_list = list()
for _ in range(0, 100):
    my_list.append(random.randint(0, 100))
print(my_list)

i = 1
count_of_intervals = 0
temp = my_list[0]
while i < len(my_list):




