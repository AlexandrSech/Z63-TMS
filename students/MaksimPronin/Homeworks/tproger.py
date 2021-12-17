from typing import Union, Any

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,]
i = 0
while a[i] <= 5:
    print(a[i])
    i += 1


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = [elem for elem in a if elem in b]
print(result)