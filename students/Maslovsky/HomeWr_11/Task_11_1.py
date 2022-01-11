class Fish:
    def __init__(self, name, size, bait):
        self.__name = name
        self.__size = size
        self.__bait = bait

    def get_name(self):
        return self.__name

    def set_size(self, size):
        if size in range(1, 11):
            self.__size = size
        elif size > 10:
            print("Хорош заливать")
        else:
            print("Неверный ввод")

    def get_size(self):
        return self.__size

    def set_bait(self, bait):
        if bait == "Пустой крючок":
            print("Не гони")
        else:
            self.__bait = bait

    def get_bait(self):
        return self.__bait

    def mesto(self):
        print("Где поймал ?")
        print("Повезло))")

    def glavnoe(self):
        print("Что самое главное на рыбалке ?" )
        input()
        print("Нет, набухаться))")

    def display_info(self):
        print(self.__name + " весом " + str(self.__size) + "кг ловится на " + self.__bait)
        self.mesto()
        self.glavnoe()





class Horse:

    def __init__(self, breet: str, age: int, color: str):
        self.__breet = breet
        self.__age = age
        self.__color = color

    @property
    def breet(self):
        return self.__breet

    @property
    def age(self):
        return self.__age

    @property
    def color(self):
        return self.__color

    @breet.setter
    def breet(self, breet):
        self.__breet = breet

    @age.setter
    def age(self, age):
        if age in range(1, 30):
            self.__age = age
        else:
            print("Недопустимый возраст")

    @color.setter
    def color(self, color):
        self.__color = color

    def run(self):
        print("Лошадка делает 'Тык-дык Тык-дык Тык-дык Тык-дык Тык-дык Тык-дык Тык-дык'")

    def display_info(self):
        print(f"Breet: {self.__breet}; \nAge: {self.__age}; \nColor: {self.__color}.")




#karas = Fish("карась", 1, "червь")
#karas.display_info()

#Molii = Horse("Pony", 10, "Red")
#Molii.display_info()
#Molii.run()



class Game:
    def __init__(self, title: str, genre: str, downloads: int):
        self.__title = title
        self.__genre = genre
        self.__downloads = downloads

    @property
    def title(self):
        return self.__title

    @property
    def genre(self):
        return self.__genre

    @property
    def downloads(self):
        return self.__downloads

    @title.setter
    def title(self, title):
        self.__title = title

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    @downloads.setter
    def downloads(self):
        self.__downloads = downloads


    def download(self):
        progress = 0
        for i in range(10):
            progress += 10
            print(str(progress) + "%")
        print("Download completed!!!")
        self.__downloads += 1

    def re_release(self):
        self.__downloads = 0
        print("Игра перевыпущена, скачайте ее заново")

BDO = Game("Black desert online", "MMORPG", 1000)



