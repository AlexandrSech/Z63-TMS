# 3) Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа 
# (пример {‘key’: ‘value’} -> {‘key3’:‘value’}). Чтобы получить список
#  ключей - использовать метод .keys()

my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
my_dict2={}
for i in my_dict:
    my_dict2.update({i + str(len(i)): my_dict[i]})

my_dict=my_dict2
print(my_dict)