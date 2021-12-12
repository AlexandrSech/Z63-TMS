# 2. Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость
# (поумолчанию 0). Методы: увеличить скорости(скорость + 5), 
# уменьшениескорости(скорость - 5), стоп(сброс скорости на 0), 
# отображение скорости,разворот(изменение знака скорости). Все атрибуты приватные.


class Car:
    def __init__(self, brand: str, model: str, year_of_release: int, speed = 0):
        self.__brand = brand
        self.__model = model
        self.__year_of_release = year_of_release
        self.__speed = speed

    @property
    def title(self):
        return self.__brand, self.__model, self.__year_of_release

    @property
    def speed(self):
        return self.__speed

    def accelerate(self):
        self.__speed +=5

    def slow_down(self):
        self.__speed -=5

    def stop(self):
        self.__speed = 0

    def revers(self):
        self.__speed = -self.__speed

    def info(self):
        print(f"Avto {self.__brand} {self.__model}, {self.__year_of_release} year of release and his speed {self.__speed} kl/h.")

if __name__ == "__main__":
    
    print("testing car")

    car = Car("Ford", "Mondeo", 2011, 60)
    car.info()
    car.accelerate()
    print(car.speed)
    car.accelerate()
    car.accelerate()
    print(car.speed)
    car.slow_down()
    print(car.speed)
    car.revers()
    print(car.speed)
    car.accelerate()
    car.stop()
    print(car.speed)

    print(f"Avto {car.title} year of release and his speed {car.speed} kl/h.")

