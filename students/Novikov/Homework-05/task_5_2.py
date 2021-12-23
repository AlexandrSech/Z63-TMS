# 2) Дано число. Найти сумму и произведение его цифр.

my_list = list(map(int, input()))
print(my_list)

sum, mult = 0, 1
for el in my_list:
    sum += el
    mult *= el

print("Сумма:", sum)
print("Произведение: ", mult)
