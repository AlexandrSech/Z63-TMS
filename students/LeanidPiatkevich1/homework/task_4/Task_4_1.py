# Task 4.1

''' Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу
умноженному на -2'''

my_list = [-5, 2, 65, -14, 8, 1, -25]

my_new_list_2 = [n * -2 for n in my_list]
print("через for", my_new_list_2)

i = 0
my_new_list_2 = []

while i < len(my_list):
    my_new_list_2.append(my_list[i] * -2)
    i += 1
print("через while", my_new_list_2)

