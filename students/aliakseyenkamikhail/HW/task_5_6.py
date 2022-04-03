# 6) Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее числобольше предыдущего).

def array_numbers(): # создаю массив из 50 чисел от 1 до 80
    import random
    array = []
    for i in range(50):
        array.append(random.randint(1, 80))
    return array
    
def find_plots(array): # определяем кол участвов с возврастающимим цифрами
    plots = []
    plot = []
    for i in range(len(array)-1):   
        if array[i] < array[i+1]:
            plot.append(array[i])        
        elif array[i] > array[i+1]:
            plot.append(array[i])        
            plots.append(plot)
            plot = []
    find_plots = len(plots)
    return plots, find_plots

array = array_numbers()
plots, find_plots = find_plots(array)
print(f"in array has {find_plots}, here they {plots}.")
        