print("Введите строку")
answer = input(" >>>")
if len(answer) >= 3:
    print(answer[0:-2])
else:
    print("Введите пожалуйста минимум 3 символа")
