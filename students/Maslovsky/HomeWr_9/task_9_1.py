spis = ["zero", "one", "two", "three", "four", "five"]
a = [str(i) + " - " + spis[i] for i in range(len(spis))]
print(a)

[print(f"{i} - {j}") for i, j in enumerate(spis)]

