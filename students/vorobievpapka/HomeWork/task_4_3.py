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

print({key + str(len(key)): value for key, value in dict.items()})

