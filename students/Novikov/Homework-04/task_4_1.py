""" 1) Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2 """

my_list = list(range(10))
print(my_list)

new_list1 = [num * -2 for num in my_list]
print(new_list1)

new_list2 = list()
counter = 0
while counter < len(my_list):
    new_list2.append(-2 * my_list[counter])
    counter += 1

print(new_list2)

