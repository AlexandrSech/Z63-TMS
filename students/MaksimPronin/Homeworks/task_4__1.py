my_list = [1, 2, 3, 4, 5]
new_list = [i * (-2) for i in my_list]
print(new_list)

my_list2 = [1, 2, 3, 4, 5]
i = 0
new_list2 = my_list2
while i < len(my_list2):
    my_list2[i] * (-2)
    print(new_list2)
    i += 1