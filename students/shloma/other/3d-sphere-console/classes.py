class Vec2:

    def __init__(self, x, y=None):
        self.__x = x
        if y is None:
            self.__y = x
        else:
            self.__y = y

    def __str__(self):
        return f"x={self.__x}, y={self.__y}"

    def __add__(self, other):
        if type(self) == type(other):
            return Vec2(self.__x + other.__x, self.__y + other.__y)
        elif type(other) in [int, float]:
            return Vec2(self.__x + other, self.__y + other)

    def __sub__(self, other):
        if type(self) == type(other):
            return Vec2(self.__x - other.__x, self.__y - other.__y)
        elif type(other) in [int, float]:
            return Vec2(self.__x - other, self.__y - other)

    def __mul__(self, other):
        if type(self) == type(other):
            return Vec2(self.__x * other.__x, self.__y * other.__y)
        elif type(other) in [int, float]:
            return Vec2(self.__x * other, self.__y * other)

    def __truediv__(self, other):
        if type(self) == type(other):
            return Vec2(self.__x / other.__x, self.__y / other.__y)
        elif type(other) in [int, float]:
            return Vec2(self.__x / other, self.__y / other)

    def __neg__(self):
        return Vec2(-self.__x, -self.__y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y


class Vec3:

    def __init__(self, x, y=None, z=None, v=None):
        self.__x = x
        if y is None and z is None and v is None:
            self.__y = x
            self.__z = x
        elif y is not None and z is not None:
            self.__y = y
            self.__z = z
        elif v is not None:
            self.__y = v.x
            self.__z = v.y

    def __str__(self):
        return f"x={self.__x}, y={self.__y}, z={self.__z}"

    def __add__(self, other):
        if type(self) == type(other):
            return Vec3(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)
        elif type(other) in [int, float]:
            return Vec3(self.__x + other, self.__y + other, self.__z + other)

    def __sub__(self, other):
        if type(self) == type(other):
            return Vec3(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)
        elif type(other) in [int, float]:
            return Vec3(self.__x - other, self.__y - other, self.__z - other)

    def __mul__(self, other):
        if type(self) == type(other):
            return Vec3(self.__x * other.__x, self.__y * other.__y, self.__z * other.__z)
        elif type(other) in [int, float]:
            return Vec3(self.__x * other, self.__y * other, self.__z * other)

    def __truediv__(self, other):
        if type(self) == type(other):
            if other.__x != 0 and other.__y != 0 and other.__z != 0:
                return Vec3(self.__x / other.__x, self.__y / other.__y, self.__z / other.__z)
            else:
                print(other)
                return Vec3(self.__x / other.__x, self.__y / -0.01, self.__z / other.__z)
        elif type(other) in [int, float]:
            return Vec3(self.__x / other, self.__y / other, self.__z / other)

    def __neg__(self):
        return Vec3(-self.__x, -self.__y, -self.__z)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    @z.setter
    def z(self, z):
        self.__z = z


if __name__ == "__main__":

    def test_fun():

        v1 = Vec2(1, 4)
        print(v1)

        v2 = Vec2(1)
        print(v2)

        v3 = Vec3(1)
        print(v3)

        v4 = Vec3(2, v=v1)
        print(v4)

        v5 = Vec3(4, 5, 6)
        print(-v5)

    test_fun()

