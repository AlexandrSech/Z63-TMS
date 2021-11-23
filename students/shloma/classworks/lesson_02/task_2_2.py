# Task 2.2

# Create list1
my_list1 = [2, 4, "a", False]
print(my_list1)

# Create list2
my_list2 = ["str", False, 2, 3.44]
print(my_list2)

# Change list1
my_list1.append("added")
my_list1.insert(0, "123")
print(my_list1)

# Change list2
my_list2.append(4)
my_list2.insert(0, True)
print(my_list2)

# Add list2 into list1
my_list1.extend(my_list2)
print(my_list1)