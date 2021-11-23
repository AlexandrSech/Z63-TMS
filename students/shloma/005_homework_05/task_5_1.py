# Task 5.1

print("Добро пожаловать в миникалькулятор!\n")

while True:
    while True:
        print("Выберите операцию:\n\t+ [сложение];\n\t- [вычитаение];\n\t* [умножение];"
              "\n\t/ [деление];\n\t0 [выход из программы].\n")

        operand = input("Желаемая операция: ")

        if operand not in "+-*/0":
            print(f"Указан неизвестный операнд {operand}\n")
            continue
        else:
            break

    if operand == "0":
        print("Выход из программы")
        break

    while True:
        x = input("Введите число x: ")
        y = input("Введите число y: ")

        if x.isdigit() and y.isdigit():
            x, y = int(x), int(y)
            break
        else:
            print(f"Для выполнения операции '{operand}' неободимо ввести числовые значения!\n")

    if operand == "+":
        z = x + y
        print(f"Сумма x = {x} и y = {y} равна {z}\n")
        continue
    elif operand == "-":
        z = x - y
        print(f"Разность x = {x} и y = {y} равна {z}\n")
        continue
    elif operand == "*":
        z = x * y
        print(f"Произведение x = {x} на y = {y} равно {z}\n")
        continue
    elif operand == "/":
        if y == 0:
            print("У православных деление на 0 не принято!\n")
            continue
        else:
            z = x / y
            print(f"Частное от x = {x} на y = {y} равно {z}\n")
            continue
    break
