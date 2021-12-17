arr = list(range(1000))

arr2 = [item for item in arr if item % 2 == 0]

arr3 = list()
for item in arr:
    # if item % 2 == 0:
    if not item % 2:
        arr3.append(item)

print(arr)
print(arr2)
print(arr3)

