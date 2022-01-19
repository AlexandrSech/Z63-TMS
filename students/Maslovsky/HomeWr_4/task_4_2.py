spis = [1,3,2,4,5,213,12,43535,2,212,4,6,7,8,9]
a = 0
for i in spis:
    if i % 2 == 0:
        a += 1
    else: continue
print(a)

c = 0
d = 0
while c < len(spis):
    b = spis[c]
    if b % 2 == 0:
        d += 1
    c += 1
print(d)