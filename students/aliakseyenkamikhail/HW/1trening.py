def pounds_in_kilograms():
    n = int(input("enter n pounds to kilograms: ")) 
    kilograms = n / 2.2
    return kilograms, n

def kilograms_in_pounds():
    n = int(input("enter n kilograms to pounds: ")) 
    pounds = n * 2.2
    return pounds, n

kilograms, n = pounds_in_kilograms()
print(f"{n} pounds = {kilograms} kilograms.")

pounds, n = kilograms_in_pounds()
print(f"{n} kilograms = {pounds} pounds.")