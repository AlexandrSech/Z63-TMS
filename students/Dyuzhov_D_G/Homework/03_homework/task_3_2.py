for guests in range(1, 60):
    print('Если колличество гостей составит', str(guests))
    if guests >=50:
        print('Заказываем ресторан')
    elif guests >=20 and guests <= 50:
        print('Заказываем кафе')
    elif guests < 20:
        print('Празднуем дома')