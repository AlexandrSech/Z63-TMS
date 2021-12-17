class Transport:
    _mass: int
    _speed: int
    _volume: int

    def load(self, v):
        self.volume = v

    def unload(self):
        x = self.volume
        self.volume = 0
        return x

    def upspeed(self):
        print("Transport")

    def downspeed(self):
        pass


class Tanker(Transport):
    def upspeed(self):
        print("tanker upspeed")


t1 = Tanker()

t1.upspeed()

exit()

class MyFirstClass:
    x: int
    y: int
    z: int

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get(self):
        return self.x, self.y, self.z

    def foo(self):
        for i in range(self.z):
            print(i)


class A2(MyFirstClass):
    def a(self):
        pass


a1 = A2()




exit()

a1 = MyFirstClass(1,2,3)
a2 = MyFirstClass()
a3 = MyFirstClass()


print(a1.get())
print(a2.get())
print(a3.get())

a3.foo()





exit()

def foo2(x:int):
    temp_list = []
    for i in range(1, x):
        if x % i == 0:
            temp_list.append(i)
    result_list = []
    for z in temp_list:
        if len(foo2(z)) == 2:
            result_list.append(z)
    return result_list




def foo(x:int):
    temp_list = []
    for i in range(1, x):
        if x % i == 0:
            temp_list.append(i)
    result_list = []
    for z in temp_list:
        for i in range(2, z-1):
            if z % i == 0:
                break
        else:
            result_list.append(z)
    return result_list

print(foo2(100))
exit()

i = "skehj sdlfkvsdlkf sdfvkl"

substrings = i.split(" ")

print(i)
print(substrings)


print(list())






exit(-1)

print(1)
exit()

my_list = [i*10 for i in range(30)]
print(my_list)

for i, elem in enumerate(my_list):
    if elem % 5:
        continue
    print(elem)
    if elem > 20:
        break
else:
    print('aloha')
