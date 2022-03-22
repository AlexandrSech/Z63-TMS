# 2) Дан список целых чисел. Подсчитать сколько четных чисел в списке

from random import randint

my_list = [randint(0, 100) for _ in range(0, 100)]
print(my_list)

cnt1 = 0
for num in my_list:
    if num % 2 == 0:
        cnt1 += 1
print(cnt1)

cnt2, i = 0, 0
while i < len(my_list):
    if my_list[i] % 2 == 0:
        cnt2 += 1
    i += 1
print(cnt2)
