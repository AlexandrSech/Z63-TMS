"""2. Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}"""

f = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}

print(f(abc=5, one="Texas"))