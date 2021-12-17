def mult(*args):
    return


def m2(x, y):
    x += y


print(mult(*[1]))



exit()




def foo1(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)
    return True


print(foo1())
print(foo1(1,2,3,4))
print(foo1(id=12, name="alex"))
print(foo1(1,2,3, id=10))


l = [
    [2, 3],
    ["hello", 5],
    # ["hello", "__"],
    # [[1], [2, 3]],
    # [{"name": "alex"}, 2]
]

for l1 in l:
    # print(l1)
    res = mult(*l1)
    # print(res)
