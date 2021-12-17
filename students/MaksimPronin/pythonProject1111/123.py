list_1 = [int(i) for i in input().split()]
povtor = ([i for i in list_1 if list_1.count(i) >= 2])
my_set = set(povtor)
print(my_set)