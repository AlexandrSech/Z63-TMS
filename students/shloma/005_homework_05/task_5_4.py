# Task 5.4

n = int(input("Введите число N: "))

s = 0
for i in range(1, n + 1):
    s += 1/i

print(f"Результирующая сумма: {s}")