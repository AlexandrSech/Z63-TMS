my_list = [1, 2, 3, 4, 5]
my_list_2 = list()
a = 1
for i in range(len(my_list)):
    if i < a:
        my_list_2.append(my_list[i])
    else:
        my_list_2.insert(i - a, my_list[i])

print(my_list_2)
