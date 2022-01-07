# 2) Дано число. Найти сумму и произведение его цифр.

n = input('enter number: ')
g = []
for i in n:
    g.append(i)

sum_ = None
for j in g:
    if sum_ == None:
        sum_ = j
    elif sum_ != None:
        sum_= int(sum_) + int(j)


print(n)
print(sum_)

composition = None
for f in g:
    if composition == None:
        composition = f
    elif composition != None:
        composition= int(composition) * int(f)

print(composition)
