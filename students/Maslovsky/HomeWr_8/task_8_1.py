def factor_2(n):
    a = 1
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            a *= i
        print("Двойной факториал:!!", n, "=", a)
    else:
        for i in range(1, n + 1, 2):
            a *= i
        print("Двойной факториал:!!", n, "=", a)


factor_2(10)
factor_2(11)
factor_2(3)
factor_2(8)
factor_2(4)