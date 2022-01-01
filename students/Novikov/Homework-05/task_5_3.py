"""3) Два натуральных числа называют дружественными, если каждое из них равно сумме всех делителей другого, кроме
самого этого числа. Найти все пары дружественных чисел, лежащих в диапазоне от 200 до 300. """


def foo(num):
    my_list = [n for n in range(1, num) if num % n == 0]
    return sum(my_list)


my_dict = dict()
for i in range(200, 301):
    for j in range(201, 301):
        if i == foo(j) and j == foo(i):
            my_dict[i] = j
            print("Дружеская пара {i} - {i2}".format(i=i, i2=my_dict[i]))
print(my_dict)
