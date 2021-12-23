"""3) Два натуральных числа называют дружественными, если каждое из них равно сумме всех делителей другого, кроме
самого этого числа. Найти все пары дружественных чисел, лежащих в диапазоне от 200 до 300. """


def foo(num):
    my_list = list()
    for n in range(1, num):
        if num % n == 0:
            my_list.append(n)
    sum = 0
    for el in my_list:
        sum += el
    return sum


my_dict = dict()
for i in range(200, 301):
    for j in range(201, 301):
        if i == foo(j) and j == foo(i):
            my_dict[i] = j
            print("Дружеская пара {i} - {i2}".format(i=i, i2=my_dict[i]))
print(my_dict)
