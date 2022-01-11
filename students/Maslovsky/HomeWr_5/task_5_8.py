stroka = "В заданной строке расположить в обратном порядке все слова"
nev_spis = []
spisok = stroka.split(" ")
print(spisok)
for i in range(len(spisok) - 1, -1, - 1):
    nev_spis.append(spisok[i])
print(nev_spis)