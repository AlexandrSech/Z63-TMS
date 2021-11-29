for guests in range(0, 60):
    if guests == 0:
        print('Если колличество гостей составит', str(guests), ' человек - свадьбы не будет!')
    elif guests == 1:
        print('Если колличество гостей составит', str(guests), ' человек - празднуем дома!')
    elif guests >=2 and guests <= 4:
        print('Если колличество гостей составит', str(guests), ' человека - празднуем дома!')
    elif guests >=5 and guests <= 50:
        print('Если колличество гостей составит', str(guests), ' человек - заказываем кафе!')
    else:
        guests < 50
        print('Если колличество гостей составит', str(guests), ' человек - заказываем ресторан')

