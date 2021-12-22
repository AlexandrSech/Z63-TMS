# 2021-12-07
# classwork

"""
Cоздайте класс с именем Restaurant
Метод init() класса Restaurant должен содержать два атрибута: restaurant_name и cuisine_type
Создайте метод describe_restaurant(), который выводит два атрибута,
и метод open_restaurant(), который выводит сообщение о том, что ресторан открыт
Создайте на основе своего класса экземпляр с именем restaurant
Выведите два атрибута по отдельности, затем вызовите оба метода
"""


class Restaurant:

    __restaurant_name: str
    __cuisine_type: str

    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.__restaurant_name = restaurant_name
        self.__cuisine_type = cuisine_type

    @property
    def restaurant_name(self):
        return self.__restaurant_name

    @property
    def cuisine_type(self):
        return self.__cuisine_type

    def describe_restaurant(self):
        print(f"Name: {self.__restaurant_name}, type: {self.__cuisine_type}")

    @staticmethod
    def open_restaurant():
        print("Restaurant open")


if __name__ == "__main__":


        restaurant = Restaurant("Diamond", "Italian")

        print(f"Name: {restaurant.restaurant_name}")
        print(f"Cuisine: {restaurant.cuisine_type}")

        restaurant.describe_restaurant()
        restaurant.open_restaurant()


