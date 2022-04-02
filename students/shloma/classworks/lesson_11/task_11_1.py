# 2022-01-11
# shlom41k


def print_matrix(matrix):
    for row in matrix:
        print(row)


l = list()
template = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 10):
    l.append(template)
    # l.append(list(template))

print_matrix(l)

l[1][1] = 1

print_matrix(l)

a = int(5)
b = int(5)

print("ID_a", id(a), "ID_b", id(b), "Совпадают" if id(a) == id(b) else "Не совпадают")


l1 = list([5])
l2 = list([5])

print("ID_a", id(l1), "ID_b", id(l2), "Совпадают" if id(l1) == id(l2) else "Не совпадают")


