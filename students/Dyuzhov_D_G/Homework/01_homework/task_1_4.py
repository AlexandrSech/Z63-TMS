'''
import math
a = 2
b = 6
n = math.sqrt(a * b)
с = (a + b)/2
print('Средне геометрическое значение чисел = ', n)
print('Средне арефметическое значение чисел = ', с)
'''


import math
def the_numbers_g (a, b):
    p = math.sqrt(a * b)
    return p
def the_numbers_n (a, b):
    c = (a + b)/2
    return c
geometry = the_numbers_g(3, 4)
arephmetics = the_numbers_n(3, 4)
print('Средне геометрическое значение чисел = ', geometry)
print('Средне арефметическое значение чисел = ', arephmetics)