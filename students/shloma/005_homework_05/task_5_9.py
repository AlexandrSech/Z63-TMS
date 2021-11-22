# Task 5.9

m = int(input("Введите число m: "))
n = int(input("Введите число n: "))

print(f"\nВсе делители на отрезке [{m}, {n}]:")

for i in range(m, n + 1):
    print(f"{i}:", end=" ")
    for j in range(2, i):
        if i % j == 0:
            print(j, end=" ")
    else:
        print("")