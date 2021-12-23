"""5) В массиве целых чисел с количеством элементов 19 определить максимальное число и
заменить им все четные по значению элементы."""
my_list = [
    20, 40, 7604, 3433, 232, 12, 3131, 3121, 13314, 1331,
    41312, 11221, 3223, 33, 3232, 2121, 12122, 2121, 1040
]
print(my_list)
max = my_list[0]
counter = 1
while counter < len(my_list):
    if max < my_list[counter]:
        max = my_list[counter]
    counter += 1

i = 0
while i < counter:
    if my_list[i] % 2 == 0:
        my_list[i] = max
    i += 1

print(my_list)




