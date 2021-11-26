# Task 8.1
# shlom41k

from random import randint


def fact2(n):
    fact = 1
    if n % 2:
        for i in range(1, n + 1, 2):
            fact *= i
    else:
        for i in range(2, n + 1, 2):
            fact *= i
    return fact


nums = [randint(1, 20) for _ in range(5)]
[print(f"Number: {n}, factorial: {fact2(n)}") for n in nums]

