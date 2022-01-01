"""9) Для каждого натурального числа в промежутке от m до n вывести все делители,
 кроме единицы и самого числа. m и n вводятся с клавиатуры."""


def find_divisors(num):
    my_list = [i for i in range(2, num) if num % i == 0]
    print(f"{num}:", end=" ")
    print(*my_list)


m = int(input("Введите первое число: "))
n = int(input("Введите второе число: "))

for num in range(m, n + 1):
    find_divisors(num)
