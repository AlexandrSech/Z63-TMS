"""Даны три слова. Выяснить, является ли хоть одно из них палиндромом ("перевертышем"),
т. е. таким, которое читается одинаково слева направо и справа налево.
(Определить функцию, позволяющую распознавать слова палиндромы.)"""


def is_palindrome(word): return word.lower() == word.lower()[::-1]


my_list = input("Введите 3 слова: ").split()

print("Есть слово палиндром") if any(is_palindrome(word) for word in my_list) else print("Нет слов-палиндромов")
