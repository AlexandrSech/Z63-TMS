# 2021-12-24

try:
    print(5 / 0)
except ZeroDivisionError as e:
    print(e)
except TypeError as err:
    print(err)
finally:
    print("Finally")