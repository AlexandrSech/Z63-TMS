a = int(input('ведите число гостей '))
if a >= 50:
    print('ресторан')
elif a in range(20, 50):
    print('кафе')
elif a <= 20:
    print('дом')