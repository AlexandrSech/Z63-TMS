def deco(foo):
    def inner(*args):
        li =list(args)
        for i in li:
            if i%2 == 0:
                li.remove(i)
        return foo(li)
    return inner

@deco
def lis(*arg):
    l = list(arg)  
    return print(l)

lis(12,3,4,5,6)