"""
4x4
"""

# array = list()

'''for _ in range(4):
    array.append([0 for _ in range(4)])'''

array = [[0 for _ in range(4)] for _ in range(4)]

for i in range(4):
    array[i][i] = 1

for i in array:
    print(i)
