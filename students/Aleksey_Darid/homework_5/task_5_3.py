f = 0
for ch in range(200, 301):
    if ch != f:
        s1 = 0
        for i in range(1, ch // 2 + 1):
            if ch % i == 0:
                s1 += i
        s2 = 0
        for j in range(1, s1 // 2 + 1):
            if s1 % j == 0:
                s2 += j
        if s2 == ch != s1:
            print(ch, s1)
            f = s1

