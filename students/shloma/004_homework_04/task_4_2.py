# Task 4.2

my_list = [0, -4, 2, 0, -4, -5, 0, 4, 13, 18, -55]

# 1) Use while
i = 0
my_new_list = []

while i < len(my_list):
    if my_list[i] % 2 == 0:
        my_new_list.append(my_list[i])
    i += 1

# 2) Use for
my_new_list2 = [n for n in my_list if n % 2 == 0]

print("Исходный список:", my_list)
print("Список четных чисел (используя while):", my_new_list)
print("Список четных чисел (используя for):", my_new_list2)

