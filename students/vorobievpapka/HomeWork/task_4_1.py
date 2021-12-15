"""
1) Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу
умноженному на -2
"""

list_= [1, 2, 3, 4, 5, 6, 7, 8]
print([num * -2 for num in list_])

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
number = 0
new_list = []
while number < len(my_list):
    new_list.append(my_list[number] * -2)
    number += 1
print(new_list)