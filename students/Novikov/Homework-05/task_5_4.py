# 4) Для заданного числа N составьте программу вычисления суммы S=1+1/2+1/3+1/4+...+1/N,
# где N – натуральное число

N = -1
while not N > 0:
    N = int(input("Введите N: "))
sum = 0
for i in range(N + 1):
    sum += 1 / i
print("Сумма ряда: ", sum)
