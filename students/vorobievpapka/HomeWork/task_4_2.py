"""
2) Дан список целых чисел. Подсчитать сколько четных чисел в списке
"""

list_ = [1, 2, 3, 4, 5, 6, 7 , 8]
new_list = [item for item in list_ if item % 2 == 0]
print(new_list)



