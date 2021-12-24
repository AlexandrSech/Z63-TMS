# 2) Дано число. Найти сумму и произведение его цифр.

my_list = list(map(int, input()))
print(my_list)

summ, mult = 0, 1
for el in my_list:
    summ += el
    mult *= el

print("Сумма:", summ)
print("Произведение: ", mult)
