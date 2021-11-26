sign = input('Введите арифметический знак')
x, y = map(int, input().split())
while sign != 0:
    if sign == '/' and y != 0:
        print(x / y)
    elif sign == '-':
        print(x - y)
    elif sign == '*':
        print(x * y)
    elif sign == '+':
        print(x + y)
    sign = input('Введите арифметический знак')
    x, y = map(int, input().split())