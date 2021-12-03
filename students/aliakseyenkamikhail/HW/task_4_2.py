# 2) Дан список целых чисел. Подсчитать сколько четных чисел в списке

n = int(input('enter numbers in list? '))
list_n= []

for i in range(n):
    list_n.append(int(input('int: ')))

even_numbers = []
for j in list_n:
    if j % 2 == 0:
        even_numbers.append(j)

sum_even_numbers = len(even_numbers)
print(sum_even_numbers)