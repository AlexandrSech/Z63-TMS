class A:
    def __init__(self):
        print("init")

    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit, exc_type={}, exc_val={}, exc_tb={}".format(exc_type, exc_val, exc_tb))

    def __str__(self):
        return "Э АЛО"


print("start")
with A() as a:
    print(a)
print("end")

