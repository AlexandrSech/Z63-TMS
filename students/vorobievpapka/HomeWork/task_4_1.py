"""
1) Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу
умноженному на -2
"""

first_list = [1, 2, 3, 4, 5, 6, 7, 8]
second_list = []
for i in first_list :
    new_znach = i * -2
    second_list.append(new_znach)

print("first list =",first_list)
print("second list =",second_list)


second_list_wh = []
z = 0
while z < len(first_list):
    new_znach2 = first_list[0] * -2
    second_list_wh.append(new_znach2)
    z += 1
    first_list[0] += 1 # как лучше записать?

print("second list =",second_list_wh)
