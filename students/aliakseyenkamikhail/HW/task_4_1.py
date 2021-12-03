# 1) Дан список целых чисел.Создать новый список, каждый 
# элемент которого равен исходному элементу умноженному на -2

n = int(input('enter numbers in list? '))
list_n = []

for i in range(n):
    list_n.append(int(input(' int: ')))

print(list_n)

list_n2 = []
for j in list_n:
    g = j * -2 
    list_n2.append(g)

print(list_n2)