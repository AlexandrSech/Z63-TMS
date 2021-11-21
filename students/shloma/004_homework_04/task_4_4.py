# Task 4.4

# Use slice
k = 1   # value of <- circshift

my_list = [0, 1, 2, 3, 4, 5, 6, 7]

my_new_list = my_list[k:] + my_list[:k]

print("List:", my_list)
print("Changed list (slice):", my_new_list)


# Use while
i = 0
my_new_list2 = []

while i < len(my_list):
    if i < k:
        my_new_list2.append(my_list[i])
    else:
        my_new_list2.insert(i - k, my_list[i])
    i += 1

print("Changed list (while):", my_new_list2)

# Use for
my_new_list3 = list()

for j in range(len(my_list)):
    if j < k:
        my_new_list3.append(my_list[j])
    else:
        my_new_list3.insert(j - k, my_list[j])

print("Changed list (for):", my_new_list3)