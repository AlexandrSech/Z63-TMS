"""
3) Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
‘value’}). Чтобы получить список ключей - использовать метод .keys()
(подсказка: создается новый ключ с цифрой в конце, старый удаляется)
"""


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
dict1 = dict.copy()
print(dict)
print(dict1)
keys = dict1.keys()
print(keys)
dict1.update(test_dict)
print(dict1)

for i in keys:
    3