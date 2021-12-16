m = 100
l = [1, 1]
while len(l) <=100:
    l.append((l[-1] + l[-2]))
print(l)