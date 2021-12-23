# 4) Дан список. Создать новый список, сдвинутый на 1 элемент влево Пример:12345-> 23451

my_list = list(range(1, 6))
print("Было: ", my_list)

my_list.append(my_list.pop(0))
print("Стало: ", my_list)