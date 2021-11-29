# Цикл For
lst1=[1,2,3,4,5,6]
u=0
for num1 in lst1:
    if num1%2==0:
        u+=1
print(u)
# Цикл While
i=0
k=0
while k<len(lst1):
    if lst1[k]%2 ==0:
        i+=1
        k+=1
    else:
        k+=1
print(i)
