# 1 Введите число. Если это число делиться на 1000 без 
# остатка, то выведите на экран "millennium"

class three():
    n: int

    def set_points(self, n):
        self.n = n
       
    def millennium(self):
        if self.n % 1000 == 0:
            return 'millenium'

a = three()
a.set_points(14000)
print(a.millennium())

