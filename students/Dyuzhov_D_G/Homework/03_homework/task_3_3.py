print('Введите сроку')
a = input()
b = len(a)
if b > 10:
    d = str('!!!')
    print('Количество символов больше 10', d)
elif b < 10:
    print('Второй символ строки =', (a[2]))
