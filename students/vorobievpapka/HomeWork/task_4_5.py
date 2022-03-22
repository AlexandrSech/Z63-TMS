"""
5) Составить список чисел Фибоначчи содержащий 15 элементов.
(Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны
либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
"""

fibonachi = [1, 1]
while len(fibonachi) <= 15:
    fibonachi.append(fibonachi[-1] + fibonachi[-2])
print(fibonachi)

fibonachi_new = [1, 1]
for i in range(14):
    fibonachi_new.append(fibonachi_new[-1] + fibonachi_new[-2])
print(fibonachi_new)