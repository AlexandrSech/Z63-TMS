import random

# Задан целочисленный массив. Определить количество участков массива, на котором элементы монотонно
# возрастают (каждое следующее число больше предыдущего).

# 1 создать массив
array = [random.randint(-100, 100) for item in range(30)]
print(array)

# search
number_of_ranges = 0
cols_items_in_range = 0
prev_item = None
for item in array:
    try:
        if item < prev_item and cols_items_in_range >= 1:
            number_of_ranges += 1
            cols_items_in_range = 0

        if item > prev_item:
            cols_items_in_range += 1
    except:
        pass
    finally:
        prev_item = item

if cols_items_in_range:
    number_of_ranges += 1


print(number_of_ranges)
