# 1. Создать пять классов описывающие реальные объекты. Каждый класс
# должен содержать минимум три приватных атрибута, конструктор, 
# геттерыи сеттеры для каждого атрибута, два метода.

class Car:
    def __init__(self, brand: str, year_of_release: int, color: str):
        self.__brand = brand
        self.__year_of_release = year_of_release
        self.__color = color

    @property
    def brand(self):
        return self.__brand

    @property
    def year_of_release(self):
        return self.__year_of_release

    @property
    def color(self):
        return self.__color

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @year_of_release.setter
    def year_of_release(self, year_of_release):
        self.__year_of_release = year_of_release

    @color.setter
    def color(self, color):
        self.__color = color

    def speed(self):
        print(f"{self.__brand} from 0 to 100 in 9.9 seconds ")

    def car_info(self):
        print(f"Brand: {self.__brand}, year of release {self.__year_of_release}, color: {self.__color}.")


class Cat:
    def __init__(self, name: str, age: int, color: str):
        self.__name = name
        self.__age = age
        self.__color = color

    @property
    def name(self):
        return self.__name

    @property 
    def age(self):
        return self.__age

    @property
    def color(self):
        return self.__color

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        if 1 < age < 25:
            self.__age = age
        else:
            print("Введен неверный возраст")

    @color.setter
    def color(self, color):
        self.__color = color

    def say(self):
        print(f"{self.__name} sey: maayyy - maaayy")

    def cat_info(self):
        print(f"name: {self.__name}, age: {self.__age}, color: {self.__color}.")
        

class Home:
    def __init__(self, adres: str, year_of_construction: int, color: str):
        self.__adres = adres
        self.__year_of_construction = year_of_construction
        self.__color = color

    @property
    def adres(self):
        return self.__adres

    @property
    def year_of_construction(self):
        return self.__year_of_construction

    @property
    def color(self):
        return self.__color

    @adres.setter
    def adres(self, adres):
        self.__adres = adres

    @year_of_construction.setter
    def year_of_construction(self, year_of_construction):
        self.__year_of_construction = year_of_construction

    @color.setter
    def color(self, color):
        self.__color = color

    def number_of_rooms(self):
        print(f"house on the {self.__adres} has 4 rooms ")

    def home_info(self):
        print(f"home is located {self.__adres}, year of construction in {self.__year_of_construction} ears, and he has {self.__color} color.")




if __name__ == "__main__":

    def testing_car():
        print("car testing: ")

        a = Car("ford", 2011, "black")
        a.car_info()
        a.speed()
        print(a.color)
        a.color = "blue"
        print(f"Brand: {a.brand}, year of release {a.year_of_release}, color: {a.color}.")

    def testing_cat():
        print("cat testing")

        b = Cat("Tihan", 8, "gray")
        b.cat_info()
        b.say()
        print(b.age)
        b.age = 9
        print(f"name: {b.name}, age: {b.age}, color: {b.color}.")

    def testing_home():
        print("home testing")

        c = Home("Siti in Misk, kozerevskaya strit", 2017, "vinous")
        c.home_info()
        c.number_of_rooms()
        print(c.color)
        c.color = "brown"
        print(f"home is located {c.adres}, year of construction in {c.year_of_construction} ears, and he has {c.color} color.")

testing_car()
testing_cat()
testing_home()