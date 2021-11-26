# Task 2.4

a = [1, 2, 3, 4]
print(f"a = {a}, id: {id(a)}")

b = []
print(f"b = {b}, id: {id(b)}")

b = a
print(f"b = {b}, id: {id(b)}")

b.append(13)
print(f"a = {a}, id: {id(a)}")
print(f"b = {b}, id: {id(b)}")