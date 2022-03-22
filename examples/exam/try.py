l = [
    {"user": 124, "token": 123},
]

for i in l:
    if i["token"] == 123:
        print(True)


exit()

primers = [x for x in range(10000) if all([x % y != 0 for y in range(2, x)])]

print(primers)


exit()

def gap(g, m, n):
    def is_prime(x):
        calls = 0
        for i in range(x - 1, 1, -1):
            if not x % i:
                calls += 1
            if calls:
                return False
        return True

    prime_list = list()
    rr = range(m, n + 1)
    for i in rr:
        if is_prime(i):
            prime_list.append(i)

    if len(prime_list) < 2:
        return []

    for i in rr:
        if i in rr and i + g in rr and i in prime_list and i + g in prime_list:
            return i, i + g


assert gap(6, 100, 110), [101, 107]


exit()


def foo(a: int = 0) -> int:
    def f(b: int = 0) -> int:
        return a + b
    return f


bar = lambda x: lambda y: x + y


def foo2(a):
    def f1(b=0):
        def f2(c=0):
            def f3(d=0):
                def f4(e=0):
                    return a + b + c + d + e
                return f4
            return f3
        return f2
    return f1


add = type("", (int, object), {"__call__": lambda s, n: add(s+n)})


print(add(1))
print(add(1)(2))
print(add(1)(2)(3))


# print(foo2(1))
# print(bar(1))


'''

'''


exit()

import time


def get_work_time(foo):
    def inner(*args, **kwargs):
        t_start = time.time()
        res = foo(*args, **kwargs)
        print(int(time.time() - t_start))
        return res
    return inner


@get_work_time
def fq(n):
    pp = 1
    for i in range(1, n+1):
        pp *= i
    return pp


def rfq(n):
    return n * rfq(n - 1) if n > 1 else 1


for i in range(100, 950):
    print(fq(i))
    ts = time.time()
    print(rfq(i))
    print(int(time.time() - ts))




exit()


def fq(n):
    pp = 1
    for i in range(1, n+1):
        pp *= i
    co = 0
    for i in str(pp)[::-1]:
        if i == "0":
            co += 1
        else:
            break
    return co

ts = time.time()
r = fq(1000)
print(r)
print((time.time() - ts))



exit()

import string

print(string.ascii_letters)
print(string.ascii_letters[:int(len(string.ascii_letters)/2)])

w = "hello world"
print(w, w.capitalize(), w.title())

exit()

l = [1,2,3,4,5,6,7,8,9]
x = iter(l)
print(list(zip(l, l)))

print(list(range(0, 10, 2)))

exit()

s = "asdfg"
print(iter(s))
print([iter(s)])
print([iter(s)] * 2)
args = [iter(s)] * 2
print(args)
print(zip(*args))

exit()

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip(*args)

s = 'asdfg'
l = [''.join(i) for i in grouper(s, 2)]
print(l)

['London', '_is_th', 'e_capi', 'tal_of', '_great', '_Brita']

exit()

iterable = "qwer"
n = 2

print([iter(iterable)])
args = [iter(iterable)] * n
print(list(zip(*args)))



exit()


a = 1
b = 2

a, b = (b, a)



exit()





def summ2(x, y):
    return x + y


def array_diff(a, b):
    return filter(lambda i: i not in b, a)


r = array_diff([1, 2], [2])
print(list(r))

exit()

b = [1,2,3,4,5, 1]

del b[b.index(1)]

print(b)

def array_diff(a, b):
    result = list()
    for a_item in a:
        if a_item not in b:
            result.append(a_item)
    '''for b_item in b:
        for a_id in range(len(a) - 1, -1, -1):
            if b_item == a[a_id]:
                del a[a_id]'''
    return result


exit()

import requests

url = "http://johnray.pythonanywhere.com/"

response = requests.get(url)
print(response, response.text)

response = requests.get(url + "get_template")
print(response, response.text)

questions = {
    "1": "",    # укажите команду в терминале для навигации по файловой системе
    "2": "",    # Укажите команду в терминале для того, чтобы узнать в какой директории сейчас вы находитесь
    "3": "",    # Укажите команду в терминале для создания папки
    "4": "",    # Укажите команду в терминале для создания файла
    "5": "",    # Укажите команду в терминале для вывода списка всех файлов и папок в текущей директории
    "6": "",    # Какой тип данных нужен для работами с целыми числами
    "7": "",    # Какой тип данных нужен для работами с дробными числами
    "8": "",    # Какой тип данных нужен для работами со строками
    "9": "",    # Какой тип данных нужен для работами с булевыми значениями
    "10": "",   # Какой оператор нужно использовать чтобы возвести число в степень
    "11": "",   # Какой оператор отвечает за целочисленные деление
    "12": "",   # Какой оператор отвечает за остаток от деления
    "13": "",   # Какой метод разделит нашу строку по указанному разделителю
    "14": "",   # Какой метод поможет нам вставлять в готовую строку в нужных местах значения переменных
    "15": "",   # Какой метод заменит указанные нами символы/подстроки на новые символы/подстроки
    "16": "",   # Что возвращают методы из предыдущих двух вопросов (ничего, строку)
    "17": "",   # Какой метод добавляет в нашу последовательность, например список, новый элемент
    "18": "",   # Какой стандартный метод нужен для получения последовательности чисел
    "19": "",   # Как узнать длину любого контейнера
    "20": "",   # Какой тип данных вернут функция из предыдущего вопроса
    "21": "",   # Какой метод возващает либо значение по ключу, либо стандартное значение в словарях
    "22": "",   # Что вернет 12 < 1
    "23": "",   # Что вернет 3 + 3 ** 3
    "24": "",   # Что вернет в if [] - True или False
    "25": "",   # Какой тип данных вернет splitlines()
    "26": "",   # Что вернет if range(10) - True или False
    "27": "",   # Какой оператор пропускает текущий шаг в цикле
    "28": "",   # Какой оператор останавливает цикл
    "29": "",   # Каким оператором возвращается значение из функции
    "30": "",   # Какой оператор не делает ничего
    "31": "",   # Какой из этих конструкций не содержит блока else: def, if, for, while, with, class
    "32": "",   # Какой метод является конструктором класса
    "33": "",   # Какой метод является деструктором класса
    "34": "",   # Какой метод вернет чтото из класса как строку
    "35": "",   # Какой символ используют для пометки что функция задекорирована
}

test = {
    "answers": questions,
    "student_name": "Alex Sech"
}


response = requests.post(url + "check", json=test)
print(response, response.text)

