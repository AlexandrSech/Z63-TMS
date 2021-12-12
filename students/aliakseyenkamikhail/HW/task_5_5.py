# 5) В массиве целых чисел с количеством элементов 19 определить максимальное 
# число и заменить им все четные по значению элементы. [02-4.1-BL19]

def getting_list(): # определяем список случайных 19 чисел 
    import random

    n=list()

    for i in range(19):
        n.append(random.randint(0, 50))
    return n

def the_largest_number(n): # находим самое более число в списке
    big_number = 0
    for i in n:
        if i > big_number:
            big_number = i
    return big_number

def replacing_numbers(n, big_number):
    replacing_list = []
    for i in n:
        i = big_number
        replacing_list.append(i)
    return replacing_list


n = getting_list()
print(n)
big_number = the_largest_number(n)
print(big_number)
replacing_list = replacing_numbers(n, big_number)
print(replacing_list)
