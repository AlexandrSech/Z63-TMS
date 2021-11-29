# Цикл For
num1=[1,2,3,4,5]
num2=[]
for i in num1:
    new_i = i*2
    num2.append(new_i)
print(num2)
# Цикл While
n=0
num3=[]
while n<len(num1):
    new_n= num1[0]*2
    num3.append(new_n)
    num1[0]+=1
    n+=1
print(num3)