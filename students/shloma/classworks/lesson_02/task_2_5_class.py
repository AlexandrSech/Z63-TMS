# Classwork
# 2021-11-26

class MyFirstClass:
    x: int
    y: int
    z: int

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def set(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get(self):
        return self.x, self.y, self.z

    def add_5(self):
        return self.x + 5, self.y + 5, self.z + 5


a1 = MyFirstClass(1, 2, 3)
a2 = MyFirstClass(1, 2, 3)
a3 = MyFirstClass(1, 2, 3)

a1.set(1, 2, 3)
a2.set(4, 5, 6)
a3.set(7, 8, 9)

# print(a1.x, a1.y, a1.z)
print(*a1.get())
print(*a2.get())
print(*a3.get())

print("\nIncrease a1 values")
a1.add_5()
print(*a1.get())