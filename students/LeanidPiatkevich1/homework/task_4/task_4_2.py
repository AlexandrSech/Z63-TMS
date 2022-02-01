# Task 4.2

''' Дан список целых чисел. Подсчитать сколько четных чисел в списке'''

my_list = [-5, 6, 2, 65, -14, 8, 1, -4, -25]
count = 0

for i in my_list:
    if i % 2 == 0:
        count += 1

print("количество чётных чисел в списке (через for) = ", count)


count1 = 0
i = 0

while i < len(my_list):
    if my_list[i] % 2 == 0:
        count1 += 1
    i += 1
print("количество чётных чисел в списке (через while) = ", count1)

