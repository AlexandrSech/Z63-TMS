# Task 5.3

a, b = 200, 300  # Search range

dels = {}

# Находим суммы делителей всех чисел из диапазона [а, b]
for n in range(a, b + 1):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    # print(f"Сумма делителей числа {n}: {sum}")
    dels[n] = sum

# Находим "дружественные" пары
for key, value in dels.items():
    for k, v in dels.items():
        if key == v and value == k:
            print(f"Дружественная пара: {key} - {k}")