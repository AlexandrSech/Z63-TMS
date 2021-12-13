def inp():
    count = 10
    while True:
        user_string = input("input here >> ")
        print(user_string)
        # if user_string == "exit":
        count -= 1
        if not count:
            return

'''
создать класс с именем ресторан метод init
этот метод должен содержать два атрибута :
restaurant_name
cuisine_type

создать метод describe_restaurant
должен выводить два атрибута 
'''


class Restaurant:
    _restaurant_name: str
    _cuisine_type: str
    _template: str

    def __init__(self, restaurant_name, cuisine_type):
        self._restaurant_name = restaurant_name
        self._cuisine_type = cuisine_type
        self._template = "{} {}"

    def __str__(self):
        return self._restaurant_name

    def describe_restaurant(self):
        return self._template.format(self._restaurant_name, self._cuisine_type)


if __name__ == '__main__':
    a = Restaurant("У Ашота", "шаурма")
    ds = a.describe_restaurant()
    print(ds)

    print(a)
    print(a.__str__())

exit()

print('start')
z = Restaurant("rest 1")
z2 = Restaurant("rest 2")
z3 = Restaurant("rest 3")
print('middle')
print(z)
print(z2)
print(z3)
print('end')