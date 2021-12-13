class A:
    name: str

    def __init__(self, _n):
        self.name = _n


class B(A):
    def __init__(self):
        super(B, self).__init__("A from B")
        print("B")


class C(B):
    def __init__(self):
        super(C, self).__init__()
        print("C")


class D:
    def __init__(self):
        self.c = C()


c = C()
print(c.name)

d = D()
print(d.c.name)
