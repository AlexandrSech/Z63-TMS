# Цикл For
list1=[1,2,3,4,5,6,7]
list2=[]
for elem in list1:
    if elem <= len(list1):
        list2.insert(-1,elem)
    else:
        list2.insert(0, elem)
print(list2)
# Цикл While
list3=[]
i=1
while i <= len(list1):
    if i <= len(list1):
        list3.insert(-1,i)
    else:
        list3.insert(0, i)
    i+=1
print(list3)
