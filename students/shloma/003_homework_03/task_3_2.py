# Task 3.2

# Количество гостей
k = int(input())

if k > 50:
    print("ресторан")
elif 20 <= k <= 50:
    print("кафе")
else:
    print("дом")