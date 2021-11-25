dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for k in list(dict.keys()) :
    dict[k + str(len(k))] = dict.pop(k)
print(dict)