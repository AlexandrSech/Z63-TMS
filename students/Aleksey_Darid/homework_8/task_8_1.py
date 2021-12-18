def fact2(n):
    i = 1
    fact_nch = 1
    fact_ch = 1
    while i <= n:
        if not i%2==0: 
            fact_nch *=i
        
        if i%2==0:
            fact_ch *= i
           
        i += 1
    print(fact_nch, fact_ch)

fact2(7)