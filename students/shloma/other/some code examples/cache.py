from functools import lru_cache
from time import time


@lru_cache(maxsize=100)
def test(num):
    result = 0
    for i in range(num):
        result += i
    return result


# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
start = time()
a = test(100000000)
print(f"Test 1: {time() - start}")

start2 = time()
a = test(100000000)
print(f"Test 2: {time() - start2}")


test(10)
test(20)
print(test.cache_info())
# print(test.cache_clear())