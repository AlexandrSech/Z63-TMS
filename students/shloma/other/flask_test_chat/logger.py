# -*- coding: utf-8 -*-

"""
Logger for server chat
"""

import os


class Logger:

    __file_name: str

    def __init__(self, file_name: str):
        self.__file_name = file_name

        if not os.path.exists(self.__file_name):
            with open(self.__file_name, "w") as fs:
                pass
        # self.change_file(file_name)

    def __del__(self):
        pass

    def add(self, text: str):
        with open(self.__file_name, "a") as fs:
            fs.write(text + "\n")

    def read(self):
        with open(self.__file_name, "r") as fs:
            return fs.read()

    def change_file(self, new_name: str):
        self.__file_name = new_name


if __name__ == "__main__":

    l = Logger("logq.log")

    print(l.read())
    l.add("123")
    print(l.read())
    l.add("123")
    print(l.read())
    l.add("123")
    print(l.read())