class Converter:

    mapping = {
        1: 'convert_inch_to_cm',
        2: 'convert_cm_to_inch',
        3: 'convert_mile_to_km',
        4: 'convert_km_to_mile',
    }

    @staticmethod
    def convert_inch_to_cm(inch):
        return inch / 2.54

    @staticmethod
    def convert_cm_to_inch(cm):
        return cm * 2.54

    @staticmethod
    def convert_mile_to_km(mile):
        return mile * 1.6

    @staticmethod
    def convert_km_to_mile(km):
        return km / 1.6



converter = Converter()
while True:
    print('Enter the number of function and the value for the conversion')
    x, y = map(int, input().split())
    if x == 0:
        break
    func = getattr(converter, converter.mapping[x])
    print(func(y))



