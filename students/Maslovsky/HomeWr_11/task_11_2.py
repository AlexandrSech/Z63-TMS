class Car:
    def __init__(self, mark: str, brand: str, year: int, speed=0):
        self.__mark = mark
        self.__brand = brand
        self.__year = year
        self.__speed = speed

    @property
    def mark(self):
        return self.__mark

    @property
    def brand(self):
        return self.__brand

    @property
    def year(self):
        return self.__year

    @property
    def speed(self):
        return self.__speed

    def gas(self):
        if self.__speed >= 0:
            self.__speed += 5
        else:
            self.__speed -= 5

    def spid_down(self):
        if self.__speed >= 0:
            self.__speed -= 5
        else:
            self.__speed += 5

    def stop(self):
        self.__speed = 0

    def speedometer(self):
        print(self.__speed)

    def revers(self):
        self.__speed = 0 - self.__speed

    def info(self):
        print(f"Mark:{self.__mark}; \nBrend:{self.__brand}; \nYear:{self.__year}; \nSpeed:{self.__speed}.")


porshe = Car("Carera", "911", 2020, 20)

porshe.gas()
porshe.speedometer()
porshe.revers()
porshe.gas()
porshe.speedometer()
porshe.spid_down()
porshe.speedometer()
porshe.revers()
porshe.info()
