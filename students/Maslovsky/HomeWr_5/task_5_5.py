spisok = [1,3,2,4,5,64,2,234,253,2,23,13,42,1,34,23,2,2,65]
m_x = max(spisok)
for i in range(len(spisok)):
    if spisok[i] % 2 == 0:
        spisok[i] = m_x
print(spisok)
