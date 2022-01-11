def dym_in_cm(p):
    return p * 2.54


def cm_in_dym(p):
    return p / 2.54


def mili_in_km(p):
    return p * 1.609344


def km_in_mili(p):
    return p / 1.609344


def funt_in_kg(p):
    return p * 0.4535923745


def kg_in_funt(p):
    return p / 0.4535923745


def unc_in_gr(p):
    return p * 28.349523125


def gr_in_unc(p):
    return p / 28.349523125


def gl_in_lit(p):
    return p * 4.546


def lit_in_gl(p):
    return p / 4.546


def pin_in_lit(p):
    return p * 0.568


def lit_in_pint(p):
    return p / 0.568


while True:
    print("\n1. Дюймы в сантиметры"
          "\n2. Сантиметры в дюймы"
          "\n3. Мили в километры"
          "\n4. Километры в мили"
          "\n5. Фунты в килограммы"
          "\n6. Килограммы в фунты"
          "\n7. Унции в граммы"
          "\n8. Граммы в унции"
          "\n9. Галлон в литры"
          "\n10. Литры в галлоны"
          "\n11. Пинты в литры"
          "\n12. Литры в пинты"
          "\n0. Выход"
          "\nВыберите номер желаемой операции:")

    n = int(input())
    if n == 0:
        break
    z = int(input("Введите численное значение:"))
    if n == 1:
        print(dym_in_cm(z))
    elif n == 2:
        print(cm_in_dym(z))
    elif n == 3:
        print(mili_in_km(z))
    elif n == 4:
        print(km_in_mili(z))
    elif n == 5:
        print(funt_in_kg(z))
    elif n == 6:
        print(kg_in_funt(z))
    elif n == 7:
        print(unc_in_gr(z))
    elif n == 8:
        print(gr_in_unc(z))
    elif n == 9:
        print(gl_in_lit(z))
    elif n == 10:
        print(lit_in_gl(z))
    elif n == 11:
        print(pin_in_lit(z))
    elif n == 12:
        print(lit_in_pint(z))



