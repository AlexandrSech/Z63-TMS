list1 = [1, 2, 3, 4, 5]
k = 0
i = 0
while k < len(list1):
    if list1[k] % 2 == 0:
        k += 1
        i += 1
    else:
        k += 1
print(i)