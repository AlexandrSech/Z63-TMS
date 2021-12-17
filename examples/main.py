# string
s = "my string"

# integer
i = 123

# float
f = 3.1415

# boolean
b = True

# containers

# Lists (списки)
my_list = [1, 2, "aijfhoieurfvosieurhv", True, []]

# Tuples (кортежи)
my_tuple = ()

# Sets (множества)
my_set = {1, 3, 3, 5, 7, 8}

# Dictionaries (словари)
my_dict = {
    "name": "alex",
    "age": 28
}

# изменяемые (списки, словари и множества)
# неизменяемые (числа, строки и кортежи)

'''var = 1
print(var, id(var))
var *= 1000
print(var, id(var))'''


d1 = {
    1: "1",
    "name": "alex",
    (1, 0, 1): "red",
    3.1415: "pi"
}

'''
v2 = 3.1415
print(id(v2), v2)
v2 *= 3
print(id(v2), v2)

print(d1)

print(type(d1))

# del d1

print(d1)
'''


v1 = range(10)
print(type(v1))

print("start loop")

for it in v1:
    print(" ", it)
    if not it % 2:
        print(it)

print("end loop")

ii = 0
while ii < 10:
    print(ii)
    if not ii % 2:
        print(ii)
    ii += 1





