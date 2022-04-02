# make func for generate list of prime numbers
def is_prime(n):
    if n == 0:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
    return True


def generate_prime_numbers(x, y):
    result = list()
    for i in range(x, y + 1):
        if is_prime(i):
            result.append(i)
    return result


print(
    [i for i in range(100, 200) if not any([i % j == 0 for j in range(2, i)])]
)


print(generate_prime_numbers(100, 200))
