# 2022-01-11
# shlom41k


def generate_prime_numbers(x, y):
    primes = []
    for n in range(x, y + 1):
        if is_prime(n):
            primes.append(n)

    return primes


def is_prime(n):
    if n == 0:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


print(generate_prime_numbers(0, 20))

a, b = 0, 20

print([n for n in range(a, b) if is_prime(n)])

print([i for i in range(a, b) if not any([i % j == 0 for j in range(2, i)])])