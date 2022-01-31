# Task 4.4

''' Дан список. Создать новый список, сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 -> 2 3 4 5 1 '''

my_list = [-5, 2, 65, -14, 8, 1, -25]

my_new_list = []
i = 0
while i < len(my_list):
    my_new_list.append(my_list[i - (len(my_list) - 1)])
    i += 1
print("через while", my_new_list)


new_my_list = list()
a = 1
for i in range(len(my_list)):
    if i < a:
        new_my_list.append(my_list[i])
    else:
        new_my_list.insert(i - a, my_list[i])

print("через for", new_my_list)
