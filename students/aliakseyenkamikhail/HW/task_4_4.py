# 4) Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 -> 2 3 4 5 1

my_spisok = [1, 2, 3, 4, 5,]

my_spisok.append(my_spisok[0])
my_spisok.pop(0)

print(my_spisok)