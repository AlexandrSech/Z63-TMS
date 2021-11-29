# Цикл For
num_fib=[1,1]
for num in num_fib:
    if num_fib[0]==0 or num_fib[1]==0:
        num_fib.append(1)
    else:
        sum1=num_fib[-1]+num_fib[-2]
        num_fib.append(sum1)
        if len(num_fib)==15:
            break
print(num_fib)
# Цикл While
num_fib2=[1,1]
i=1
while i<=13:
    if num_fib2[0]==0 or num_fib2[1]==0:
        num_fib2.append(1)
        i+=1
    else:
        sum2=num_fib2[-1]+num_fib2[-2]
        num_fib2.append(sum2)
        i+=1
print(num_fib2)