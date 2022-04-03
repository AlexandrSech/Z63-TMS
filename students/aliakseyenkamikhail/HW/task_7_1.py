# 1. Написать 12 функций по переводу:1. Написать 12 функций по переводу:
#  1 Дюймы в сантиметры
#  2 Сантиметры в дюймы
#  3 Мили в километры
#  4 Километры в мили
#  5 Фунты в килограммы
#  6 Килограммы в фунты
#  7 Унции в граммы
#  8 Граммы в унции
#  9 Галлон в литры
#  10 Литры в галлоны
#  11 Пинты в литры
#  12 Литры в пинты

def inches_to_centimeters(): #
    n = int(input("enter n inches to centimeters: ")) 
    centimeters = n * 2.54
    return centimeters, n

def centimeters_to_inches(): #
    n = int(input("enter n centimeters to inches: ")) 
    inches = n / 2.54
    return inches, n


def miles_in_kilometers():
    n = int(input("enter n miles to kilometers: ")) 
    kilometers = n * 1.61
    return kilometers, n

def kilometers_in_miles():
    n = int(input("enter n ilometers to miles: ")) 
    miles = n / 1.61
    return miles, n

def pounds_in_kilograms():
    n = int(input("enter n pounds to kilograms: ")) 
    kilograms = n / 2.2
    return kilograms, n

def kilograms_in_pounds():
    n = int(input("enter n kilograms to pounds: ")) 
    pounds = n * 2.2
    return pounds, n


centimeters, n= inches_to_centimeters()
print(f"{n} inches = {centimeters} centimeters.")

inches, n = centimeters_to_inches()
print(f"{n} centimeteres = {inches} inchers.")

kilometers, n = miles_in_kilometers()
print(f"{n} inches = {kilometers} kilometers.")

miles, n = kilometers_in_miles()
print(f"{n} kilometers = {miles} miles.")

kilograms, n = pounds_in_kilograms()
print(f"{n} pounds = {kilograms} kilograms.")

pounds, n = kilograms_in_pounds()
print(f"{n} kilograms = {pounds} pounds.")