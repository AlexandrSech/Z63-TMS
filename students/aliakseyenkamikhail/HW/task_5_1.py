# 1) Написать программу, в которой вводятся два операнда Х и Y и знак операции
# sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
# реакции на возможный неверный знак операции, а также на ввод Y=0 при делении. 
# Организовать возможность многократных вычислений без перезагрузки
# программа (т.е. построить бесконечный цикл). В качестве символа прекращения
# вычислений принять ‘0’ (т.е. sign='0').

def enter_numers_sing():
    
    x = int(input(' enter number x int or float: '))
    y = int(input(' enter number y int or float: '))
    sing = input(' enter sing: +, –, / or  * ')
    
    return x, y, sing

def count(x, y, sing):
    if sing == '+':
        z = x+y
    elif sing == '-':
        z = x-y
    elif sing == '*':
        z = x*y
    elif sing == '/':
        z = x/y
    return z

x, y, sing = enter_numers_sing()
print(x, y, sing)
z = count(x, y, sing)
print(z)