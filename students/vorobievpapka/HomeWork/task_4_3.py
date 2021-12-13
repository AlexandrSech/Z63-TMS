"""
3) Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
‘value’}). Чтобы получить список ключей - использовать метод .keys()
(подсказка: создается новый ключ с цифрой в конце, старый удаляется)
"""
# {(k + len(k)): v for k,v in test_dict.items()}

dict = {
    'test': 'test_value',
    'europe': 'eur',
    'dollar': 'usd',
    'ruble': 'rub'

}

test_dict = {
    'name': 'Artsem',
    'age': '20',

}
# dict1 = dict.copy()
# print(dict)
# print(dict1)
# keys = dict1.keys()
# print(keys)
# dict1.update(test_dict)
# print(dict1)
#
# for i in keys:
#     3
# b = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# print({key + str(len(key)): value for key, value in b.items()})
# for k, v in b.items():
#     print('key', k)
#     print('value', v)
#
# print(list(b.keys()))
# print(b.values())
# print(b.items())
# a = 1, 2
a, b = (2, 3)
print(a, b)