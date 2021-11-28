string1=str(input("Введите строку "))
l=len(string1)
n=l/2
n=int(n)
print(string1[n])
if string1[n]==string1[0]:
    string_cut=string1[1:-1]
    print(string_cut)