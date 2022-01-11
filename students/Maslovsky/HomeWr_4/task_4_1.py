a = [9,2,3,4,55555,6,7,8,9,0]
new_spis = []
for i in a:
    b = i * (-2)
    new_spis.append(b)
print(new_spis)


new_spis_1 = [i * (-2)for i in a]
print(new_spis)

p = 0
new_spis_2 = []
while p < len(a):
    x = a[p]
    r = x * (-2)
    p += 1
    new_spis_2.append(r)
print(new_spis_2)


