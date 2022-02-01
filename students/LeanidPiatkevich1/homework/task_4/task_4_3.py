# Task 4.3

''' Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
‘value’}). Чтобы получить список ключей - использовать метод .keys()
(подсказка: создается новый ключ с цифрой в конце, старый удаляется)'''

my_dictionary = {'test': 'test_value',
                'europe': 'eur',
                'dollar': 'usd',
                'ruble': 'rub'
                }
my_dictionary_2 = dict(my_dictionary)

for key in list(my_dictionary.keys()):
    my_dictionary[key + str(len(key))] = my_dictionary.pop(key)
print("с использованием for: ", my_dictionary)


keys = list(my_dictionary_2.keys())
i = 0

while i < len(keys):
    my_dictionary_2[keys[i] + str(len(keys[i]))] = my_dictionary_2.pop(keys[i])
    i += 1
print("с использованием while: ", my_dictionary_2)



