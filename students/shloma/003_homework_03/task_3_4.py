# Task 3.4

# Input string
s = input()

# Search center of the input string
if len(s) % 2:
    ind_mean = int(len(s) / 2)
    # print(s[ind_mean])
else:
    ind_mean = int(len(s) / 2 - 1)
    # print(s[ind_mean])

# If central symbol == first symbol
if s[ind_mean] == s[0]:
    s_new = s[1:-1]
    print(s_new)
