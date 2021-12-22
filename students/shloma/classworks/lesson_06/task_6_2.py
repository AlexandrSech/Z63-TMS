# 2021-12-10
# classwork

"""
Файл из 100 строк
в каждой строке порядковый номер строки * 100
"""

n = 100

with open("numbers.log", "w", encoding="utf-8") as f:
    [f.write((str(i) + " ") * n + "\n") for i in range(n + 1)]


with open("numbers.log", "r", encoding="utf-8") as f:
    text = f.read()
    text2 = f.read()
    # print(text)

    for line in text.splitlines():
        print(line)

    print("Text2", text2)