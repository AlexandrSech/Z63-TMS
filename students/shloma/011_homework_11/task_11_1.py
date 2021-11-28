# Task 11.1
# shlom41k

class Cat:
    def __init__(self, name: str, age: int, color: str):
        self.__name = name
        self.__age = age
        self.__color = color

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def set_age(self, age):
        if 1 < age < 25:
            self.__age = age
        else:
            print("Введен неверный возраст")

    def set_name(self, name):
        self.__name = name

    def set_color(self, color):
        self.__color = color

    def say_meow(self):
        print(f"{self.__name} say: meow-meow")

    def disp_info(self):
        print(f"Name: {self.__name}; age: {self.__age}; color: {self.__color}")


class Car:
    def __init__(self, brand, model, power, color):
        self.__brand = brand
        self.__model = model
        self.__power = power
        self.__color = color

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_power(self):
        return self.__power

    def get_color(self):
        return self.__color

    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_power(self, power):
        self.__power = power

    def change_color(self, color):
        if color.lower() in ["red", "green", "blue", "yellow", "black", "white", "gray"]:
            self.__color = color
        else:
            print("Error: Forbidden color")

    def get_info(self):
        print(f"Brand: {self.__brand}, model: {self.__model}, power: {self.__power}, color: {self.__color}")

    def honk(self):
        print(f"{self.__brand} {self.__model} say: Beeeeep-beeeeeep")


class FPGA:
    def __init__(self, type: str, family: str, name: str, luts: int, package="FFVB900"):
        self.__type = type
        self.__family = family
        self.__name = name
        self.__luts = luts
        self.__available_loots = luts
        self.__package = package

    def get_type(self):
        return self.__type

    def get_family(self):
        return self.__family

    def get_name(self):
        return self.__name

    def get_luts_status(self):
        return self.__luts, self.__available_loots

    def get_package(self):
        return self.__package

    def set_type(self, type: str):
        self.__type = type

    def set_name(self, name: str):
        self.__name = name

    def set_family(self, family):
        self.__family = family

    def set_luts(self, luts: int):
        self.__available_loots = self.__available_loots + (luts - self.__luts)
        self.__luts = luts

    def hold_luts(self, luts: int):
        if self.__available_loots - luts < 0:
            print(f"Don't have {luts} free luts. Now {self.__available_loots} are available")
        else:
            self.__available_loots -= luts

    def reset_loots(self):
        self.__available_loots = self.__luts

    def set_package(self, package: str):
        if package in ["FFVB900", "FFVB1560", "FFVB676", "FFVT900", "FFVT1156", "BGA900"]:
            self.__package = package
        else:
            print("Error! This type of package doesn't exists")


class Computer:
    def __init__(self, type: str, processor: str, memory_size: int, video_adapter: str):
        self.__type = type
        self.__processor = processor
        self.__memory_size = memory_size
        self.__video_adapter = video_adapter
        self.__free_memory = memory_size

    def get_type(self):
        return self.__type

    def get_proc(self):
        return self.__processor

    def get_memory_size(self):
        return self.__memory_size

    def get_free_memory(self):
        return self.__free_memory

    def get_video_adapter(self):
        return self.__video_adapter

    def run_task(self, mem_size: int):
        if self.__free_memory < mem_size:
            print("Error: Not enough memory")
        else:
            self.__free_memory -= mem_size

    def close_task(self, mem_size: int):
        if self.__memory_size < mem_size:
            self.__free_memory = self.__memory_size
        elif self.__free_memory + mem_size > self.__memory_size:
            self.__free_memory = self.__memory_size
        else:
            self.__free_memory += mem_size

    def clear_memory(self):
        self.__free_memory = self.__memory_size

    def get_info(self):
        print(f"{self.__type}, processor: {self.__processor}, "
              f"total memory: {self.__memory_size} MB, free memory: {self.__free_memory} MB")


class Gun:
    def __init__(self, model: str, weight: float, distance: int, magazin=9):
        self.__model = model
        self.__magazin = magazin
        self.__shots = magazin
        self.__weight = weight
        self.__distance = distance

    def get_model(self):
        return self.__model

    def get_weight(self):
        return self.__weight

    def get_distance(self):
        return self.__distance

    def get_patrons_info(self):
        return self.__shots

    def magazin_size(self):
        return self.__magazin

    def set_model(self, model: str):
        self.__model = model

    def set_weight(self, weight: float):
        self.__weight = weight

    def set_distance(self, len: int):
        self.__distance = len

    def set_magazin_size(self, size: int):
        self.__magazin = size
        self.__shots = size

    def shot(self):
        if self.__shots > 0:
            self.__shots -= 1
            print("Pif-puf")
        else:
            print("No patrons! Reload right now!")

    def reload(self):
        self.__shots = self.__magazin

    def show_info(self):
        print(f"{self.__model}, patrons: {self.__shots}, distance = {self.__distance}")


if __name__ == "__main__":

    def testing_cat():
        print("Cat Testing")

        M = Cat("Tom", 4, "black")

        M.disp_info()
        M.say_meow()

    def testing_car():
        print("Car Testing")

        C = Car("Honda", "Civik", 160, "red")

        C.honk()
        C.get_info()
        C.change_color("cyan")
        C.get_info()
        C.change_color("gray")
        C.get_info()

    def testing_fpga():
        print("FPGA Testing")

        kc410 = FPGA("FPGA", "Kintex-7", "KC410T", 5600, "BGA900")

        print(kc410.get_type(), kc410.get_family(), kc410.get_name(), kc410.get_package())
        print(kc410.get_luts_status())
        kc410.hold_luts(5000)
        print(kc410.get_luts_status())
        kc410.hold_luts(500)
        print(kc410.get_luts_status())
        kc410.hold_luts(200)
        kc410.reset_loots()
        print(kc410.get_luts_status())
        kc410.hold_luts(500)
        print(kc410.get_luts_status())
        kc410.set_luts(7000)
        print(kc410.get_luts_status())

    def testing_comp():
        print("Computer Testing")

        my_pc = Computer("Notebook", "Core i7 10-th GEN", 16000, "Nvidia GForce MX250")

        my_pc.get_info()
        my_pc.run_task(500)
        my_pc.get_info()
        my_pc.run_task(1000)
        my_pc.get_info()
        my_pc.close_task(100)
        my_pc.get_info()
        my_pc.close_task(3000)
        my_pc.get_info()
        my_pc.run_task(2300)
        my_pc.get_info()
        my_pc.clear_memory()
        my_pc.get_info()

    def testing_gun():
        print("Gun Testing")

        gun = Gun("Makarov", 0.9, 100)

        gun.show_info()
        gun.shot()
        gun.shot()
        gun.show_info()
        gun.shot()
        gun.shot()
        gun.shot()
        gun.shot()
        gun.shot()
        gun.shot()
        gun.shot()
        gun.shot()
        gun.show_info()
        gun.reload()
        gun.show_info()
        gun.shot()

    # Testing
    testing_cat()
    print()
    testing_car()
    print()
    testing_fpga()
    print()
    testing_comp()
    print()
    testing_gun()