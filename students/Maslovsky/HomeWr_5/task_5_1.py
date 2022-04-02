flag = 1
s = 0
while True:
    print("Введите число:")
    x = int(input())
    while flag == 1:
        print("Введите второе число:")
        y = int(input())
        '''if y == 0:
            print("Введено неверное значение!")
            continue
        else:
            flag = 2
        flag = 1'''
        while flag == 1:
            print("Выберете операцию: '+' '-' '*' '/'")
            op = input()
            if op == "+":
                s = x + y
                flag = 2
            elif op == "-":
                s = x - y
                flag = 2
            elif op == "*":
                s = x * y
                flag = 2
            elif op == "/":
                if y == 0:
                    print("На ноль делить нельзя")
                    continue
                else:
                    s = x / y
                    flag = 2
            else:
                print("Выбрана неверная операция!!!")
                continue
    flag = 1
    print(x, op, y, "=", s)
