# Введите число. Если это число делится на 1000 без остатка, то выведите на экран "millennium"

num = int(input("Input your number: "))

if num % 1000 == 0:
    print("millennium")
