# начало 4,10,2021
#  1 Ввсети н строк с консолиб найти самую короткую и самую длинную 
n = int(input(' Enter n lines'))
x = []

for i in range(n):
    x.append(input('inp: '))

max_=''
min_=x[0]

for i in x:
    if len(i) >= len(max_):
        max_= i
    if len(i) < len(min_):
        min_ = i
print('hello')
print(min_, len(min_))
print(max_, len(max_))

