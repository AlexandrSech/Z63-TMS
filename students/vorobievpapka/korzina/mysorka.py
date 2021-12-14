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











print([num % 2 for num in list])



# print([num * -2 for num in first_list])

# list = [1, 2, 3, 4, 5, 6, 7, 8,]
# numbers = 0
# for i in list:
#     if i % 2 == 0:
#         numbers += 1
#
# print(numbers)
#
# print("--------------------------------")
#
# list1 = [1, 2, 3, 4, 5, 6, 7, 8,]
# z = 0
# num = 0
# print(list1)
# while z < len(list1):
#     if list1[0] % 2 ==0:
#         num += 1
#     list1[0] += 1 # проблема в этой записи
#     z += 1
#
# print(num)
# print(list1) # Выводит [9, 2, 3, 4, 5, 6, 7, 8] , почему вместо 1 стоит 9?