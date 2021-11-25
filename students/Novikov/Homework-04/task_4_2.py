# 2) Дан список целых чисел. Подсчитать сколько четных чисел в списке

my_list = list(range(3, 17, 3))
print(my_list)

counter1 = 0
for num in my_list:
    if not num % 2:
        counter1 += 1
print(counter1)

counter2 = 0
i = 0
while i < len(my_list):
    if not my_list[i] % 2:
        counter2 += 1
    i += 1
print(counter2)
