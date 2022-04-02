def decor_numb(func):
    def work(my_spis: list):
        [my_spis.pop(i) for i, v in enumerate(my_spis) if not v % 2]
        func(my_spis)
    return work


@decor_numb
def numb(my_spis: list):
    print(my_spis)


spis = [1, 2, 3, 4, 5, 6, 7, 8]

numb(spis)



