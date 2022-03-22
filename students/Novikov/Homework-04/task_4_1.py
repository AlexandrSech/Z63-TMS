""" 1) Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2 """

from random import randint

my_list = [randint(-20, 20) for _ in range(0, 20)]
print(my_list)

new_list1 = [num * -2 for num in my_list]
print(new_list1)

new_list2 = list()
counter = 0
while counter < len(my_list):
    new_list2.append(-2 * my_list[counter])
    counter += 1
print(new_list2)

new_list3 = list()
for i in range(len(my_list)):
    new_list3.append(-2 * my_list[i])
