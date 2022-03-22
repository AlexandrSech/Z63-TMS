def polindrom_li(my_list: list):
    for a in my_list:
        if a.lower() == a.lower()[::-1]:
            print(a, "- является полиндромом")
        else:
            print(a, "- не является полиндромом")


spis = ["abvcxcvba", "djafgkaf", "assa", "qwerttrewq"]

polindrom_li(spis)
