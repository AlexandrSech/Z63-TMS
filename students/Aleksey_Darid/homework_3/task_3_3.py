string1=str(input("Ведите строку "))
if len(string1) > 10:
    n = "!!!"
    new_string = string1 + n
    print(new_string)
else:
    print(string1[1])