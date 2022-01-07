# 5) Составить список чисел Фибоначчи содержащий 15 элементов.

fibonacci_while = [1, 1,]

while len(fibonacci_while) <= 15:
    fibonacci_while.append(fibonacci_while[-1] + fibonacci_while[-2])

print(fibonacci_while)    

fibonacci_for = [1, 1,]

for i in range(14):
    fibonacci_for.append(fibonacci_for[-2] + fibonacci_for[-1])

print(fibonacci_for)