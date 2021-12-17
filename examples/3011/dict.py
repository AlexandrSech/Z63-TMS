x = [1, 2, 3, 4, 5, 6, 7]
x += [x.pop(0)]
x += x.pop(0)
print(x)




exit()

def my_pop(__list=[], __index=0):
    r = __list[__index]
    del __list[__index]
    return r


l = [1,2,3,4,5,6,]

print(l)
print(l.append(my_pop(l, 0)))
print(l)

exit()

my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
d = dict()
for key, value in my_dict.items():
    # print(z, len(z),  my_dict[z])
    d[key + str(len(key))] = value

my_dict = d

print(my_dict)

print(my_dict.keys())
print(my_dict.items())
print(my_dict.values())


