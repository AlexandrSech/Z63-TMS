# Цикл For
dict1= {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
z=list(dict1.keys())
for k in z:
    dict1[k+ str(len(k))] = dict1.pop(k)
print(dict1)
# Цикл While
dict2= {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
p=list(dict2.keys())
i=0
while i<len(p):
    dict2[p[i] + str(len(p[i]))] = dict2.pop(p[i])
    i+=1
print(dict2)

