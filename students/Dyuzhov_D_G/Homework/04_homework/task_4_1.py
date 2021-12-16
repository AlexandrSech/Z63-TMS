my_list = range(100)
my_list_new = []
for i in my_list:
    if i % 2 == 0:
        my_list_new.append(my_list[i])
print("Список четных чисел из списка =", my_list_new)
print("Колличество четных чисел из списка=", len(my_list_new))