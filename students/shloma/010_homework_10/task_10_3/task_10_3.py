# Task 10.3
# shlom41k

"""
1) Функция write_to_file() записывает в файл список строк (подается в качестве аргумента).
2) Функция read_from_file() считывает все строки из файла и возвращает их в виде списка строк
   (предварительно удаляя символы "\n").
3) Функция generate_dates() является необязательной. Предназначена для генерации случайного
   списка дат и зиписи его в файл.
"""


from datetime import *
from random import randint


# my_fun for write to file
def write_to_file(filenme, data, method='w'):
    with open(filenme, method) as f:
        f.writelines(data)


# my_fun for read from file
def read_from_file(filename):
    with open(filename) as f:
        d = f.readlines()
        return list(map(str.strip, d))


# me_fun for generate random dates
def generate_dates(file):
    # Generates some random dates
    dates = [f"{randint(1900, 2021)}-{randint(1, 12)}-{randint(1, 28)}\n" for _ in range(500)]

    # Write dates to file
    write_to_file(file, dates, "w")


if __name__ == "__main__":

    # File with input data
    file = "dates.txt"

    # Regenerate data into a file
    generate_dates(file)    # Comment/uncomment

    # Read data from file
    dat = read_from_file(file)

    # Search earliest date
    earliest = datetime.strptime(dat[0], "%Y-%m-%d")

    for data in dat:
        if datetime.strptime(data, "%Y-%m-%d") < earliest:
            earliest = datetime.strptime(data, "%Y-%m-%d")

    print(f"Earliest date: {earliest.year}-{earliest.month}-{earliest.day}")


