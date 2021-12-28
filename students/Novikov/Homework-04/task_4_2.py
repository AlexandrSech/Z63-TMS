# 2) Дан список целых чисел. Подсчитать сколько четных чисел в списке

from random import randint

my_list = list()
for _ in range(0, 100):
    my_list.append(randint(0, 100))
print(my_list)

counter1 = 0
for num in my_list:
    if num % 2 == 0:
        counter1 += 1
print(counter1)

counter2 = 0
i = 0
while i < len(my_list):
    if my_list[i] % 2 == 0:
        counter2 += 1
    i += 1
print(counter2)
