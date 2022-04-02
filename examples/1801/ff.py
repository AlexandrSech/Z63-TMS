cache = {0: 0, 1: 1}
count = 0


def deco(f):
    def inner(n):
        global count
        count += 1

        if n in cache.keys():
            return cache[n]
        else:
            res = f(n)
            cache[n] = res
            return res
    return inner


def checker(n):
    # проверяет есть ли по такому номеру в кэшэ значение
    # если есть - возвращает
    if n in cache.keys():
        return cache[n]
    # если нет - fib(n)
    else:
        res = fib(n)
        cache[n] = res
        return res


@deco
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)


def fib2(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)


for n in range(100):
    r = fib(n)
    print(r, fib2(n))
    print(count)
    print(cache)
