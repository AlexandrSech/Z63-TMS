# 3) Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа.
# Найти всепары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]

a = 200
b = 300 

dels = {}

for n in range(a, b + 1): # находим сумму делителей каждого числа
    sum = 0
    for i in range(1, n):
        if n%i == 0:
            sum +=i
    dels[n] = sum
# print(dels) # выводим все числа и сумму их делителей

friendly_couple = {} # находи дружественные числа
for key, value in dels.items():
    for k, v in dels.items():
        if key == v and value == k:
            friendly_couple[key] = k
            
print(f"Friendly couple: {friendly_couple}.")
