# Task 8.2
# shlom41k

# Проверяем слово
def is_word_polyndrom(word):
    return True if word.lower() == word.lower()[::-1] else False


# Проверяем строку
def is_str_polyndrom(s):
    s = s.replace(" ", "")
    return True if s.lower() == s.lower()[::-1] else False


words = ["lol", "топот", "lolli", "powop", "student"]
s = "А роза упала на лапу Азора"

[print(f"'{word}' {'is poly' if is_word_polyndrom(word) else 'is not poly'}") for word in words]
print(f"\n'{s}' {'is poly string' if is_str_polyndrom(s) else 'is not poly string'}")
