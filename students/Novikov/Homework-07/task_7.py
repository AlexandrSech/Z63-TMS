"""1. Написать 12 функций по переводу:
    1. Дюймы в сантиметры
    2. Сантиметры в дюймы
    3. Мили в километры
    4. Километры в мили
    5. Фунты в килограммы
    6. Килограммы в фунты
    7. Унции в граммы
    8. Граммы в унции
    9. Галлон в литры
    10. Литры в галлоны
    11. Пинты в литры
    12. Литры в пинты"""


def inches_to_centimeters(inches):
    return inches * 2.54


def centimeters_to_inches(centimeters):
    return centimeters / 2.54


def miles_to_kilometers(miles):
    return miles * 1.609


def kilometers_to_miles(kilometers):
    return kilometers / 1.609


def pounds_to_kilograms(pounds):
    return pounds / 2.205


def kilograms_to_pounds(kilograms):
    return kilograms * 2.205


def ounces_to_grams(ounces):
    return ounces / 28.35


def grams_to_ounces(grams):
    return grams * 28.35


def gallons_to_liters(gallons):
    return gallons / 3.7854


def liters_to_gallons(liters):
    return liters * 3.7854


def pints_to_liters(pints):
    return pints / 2.113


def liters_to_pints(liters):
    return liters * 2.113


while True:
    num = -1
    print("1. Дюймы в сантиметры\n"
          "2. Сантиметры в дюймы\n"
          "3. Мили в километры\n"
          "4. Километры в мили\n"
          "5. Фунты в килограммы\n"
          "6. Килограммы в фунты\n"
          "7. Унции в граммы\n"
          "8. Граммы в унции\n"
          "9. Галлон в литры\n"
          "10. Литры в галлоны\n"
          "11. Пинты в литры\n"
          "12. Литры в пинты\n"
          )
    while not 1 <= num <= 12:
        num = int(input("Введите число: "))
    n = float(input("Введите число для конвертации: "))
    if num == 1:
        print(f"{n} дюймов - это {inches_to_centimeters(n)} сантиметров ")
    elif num == 2:
        print(f"{n} сантиметров - это {centimeters_to_inches(n)} дюймов ")
    elif num == 3:
        print(f"{n} миль - это {miles_to_kilometers(n)} километров ")
    elif num == 4:
        print(f"{n} километров - это {kilometers_to_miles(n)} миль ")
    elif num == 5:
        print(f"{n} фунтов - это {pounds_to_kilograms(n)} килограммов ")
    elif num == 6:
        print(f"{n} килограммов - это {kilograms_to_pounds(n)} фунтов ")
    elif num == 7:
        print(f"{n} унций - это {ounces_to_grams(n)} граммов ")
    elif num == 8:
        print(f"{n} граммов - это {grams_to_ounces(n)} унций ")
    elif num == 9:
        print(f"{n} галлонов - это {gallons_to_liters(n)} литров ")
    elif num == 10:
        print(f"{n} литров - это {liters_to_gallons(n)} галлонов ")
    elif num == 11:
        print(f"{n} пинт - это {pints_to_liters(n)} литров ")
    elif num == 12:
        print(f"{n} литров - это {liters_to_pints(n)} пинт ")
    if input("Если хотите выйти из программы, нажмите 0: ") == "0":
        print("Выход")
        break
