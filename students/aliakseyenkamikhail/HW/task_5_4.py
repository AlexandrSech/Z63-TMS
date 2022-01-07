# 4) Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число. [02-3.2-ML21]

while True:
    n = input("Enter number: int: ")
    if n.isdigit():
        n = int(n)
        break

print(f"You enter number: {n}.")
sum = []
a = 0
for i in range(10):
    a +=1
    b = i + a
    sum.append(b/n)
print(sum)

