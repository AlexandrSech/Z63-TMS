print("Введите количество людей:")
a = int(input())
if a > 50:
    print("Restaurant")
elif 20 <= a <= 50:
    print("cafe")
elif a < 20:
    print("home")

a = int(input())
if a in range (20):
    print("home")
elif a in range (20, 50):
    print("cafe")
else: print("restaurant")