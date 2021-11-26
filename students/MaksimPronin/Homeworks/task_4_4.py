list = [1, 2, 3, 4, 5]
new_list = []
i = 0
while i < len(list):
    new_list.append(list[i - (len(list) - 1)])
    i += 1
print(new_list)