# 2021-12-24

import random


array = [random.randint(-100, 100) for _ in range(10)]

print(array)

number_of_ranges = 0
cols_item = 0

prev_item = None

for item in array:
    try:
        if item < prev_item and cols_item >= 1:
            number_of_ranges += 1
            cols_item = 0

        if item > prev_item:
            cols_item += 1

    except Exception as e:
        print(e)
    finally:
        prev_item = item

if cols_item:
    number_of_ranges += 1

print(number_of_ranges)