# Task 4.5

n = 15  # Fibonacci length

# Use while
fib_list = [1]

i = 1       # Loops counter
prev = 0    # Previous number
cur = 1     # Current number

while i < n:
    prev, cur = cur, prev + cur
    fib_list.append(cur)
    i += 1

print("\nFibonacci (use while):\n", fib_list)


# Use for
fib_list2 = [1]

prev = 0
cur = 1

for i in range(1, n):
    prev, cur = cur, prev + cur
    fib_list2.append(cur)

print("\nFibonacci (use for:)\n", fib_list2)