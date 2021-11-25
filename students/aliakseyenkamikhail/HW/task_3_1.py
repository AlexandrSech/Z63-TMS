# 1 Введите число. Если это число делиться на 1000 без 
# остатка, то выведите на экран "millennium"

n = int(input('enter number '))

if n % 1000 == 0:
    print('millennium')