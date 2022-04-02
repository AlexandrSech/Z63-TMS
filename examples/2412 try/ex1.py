class MyException(Exception):
    def __str__(self):
        return "this is my exeption biech"


try:
    raise MyException
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except Exception as my_ex:
    print(my_ex.args, my_ex)
finally:
    print("finally")
