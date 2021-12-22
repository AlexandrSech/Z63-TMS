# 2021-12-10
# classwork

"""
Create array
"""
n = 4

array = [[0] * n] * n
array2 = [[0 for _ in range(n)] for _ in range(n)]

print(array)
print(array2)

for i in array:
    print(*i)
