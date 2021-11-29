import math
a = 2
b = 6
n = math.sqrt(a * b)
с = (a + b)/2
print('Средне геометрическое значение чисел = ', n)
print('Средне арефметическое значение чисел = ', с)


exit()

import math
def the_numbers_g (a, b):
    p = math.sqrt(a * b)
    c = (a + b) / 2
    return p, c

geometry, arephmetics = the_numbers_g(4, 6)

print('Средне геометрическое значение чисел = ', geometry)
print('Средне арефметическое значение чисел = ', arephmetics)

