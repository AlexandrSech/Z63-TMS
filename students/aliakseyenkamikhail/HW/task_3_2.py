# 2) В семье N свадьба. Они решили выбрать заведение, где будут праздновать 
# взависимости от количества людей, которое прибудет к утру.
# Если их будет больше 50 - закажут ресторан, если от 20 до 50 -то кафе, 
# а еслименьше 20 то отпраздную дома Вывести "ресторан", "кафе", "дом" в 
# зависимости от количества гостей (прочитатьпеременную с консоли)

number_of_guests = int(input('Enter number of guests '))

if number_of_guests > 50:
    print (f'restaurant for {number_of_guests}')
elif 20 <= number_of_guests <= 50:
    print(f'cafe for {number_of_guests}')
else:
    print(f'home for {number_of_guests}')