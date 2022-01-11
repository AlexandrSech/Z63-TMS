m, n = int(input()), int(input())
deliteli = []

for i in range(m, n+1):
    for j in range(2, i):
        if i % j == 0:
            deliteli.append(j)
    print(i, ":", *deliteli)
    deliteli = []

