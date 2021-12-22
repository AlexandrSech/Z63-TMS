# 2021-12-10
# classwork
# WITH

class A:
    def __init__(self):
        print("Init")
        pass

    def __enter__(self):
        print("Enter")
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit: exc_type={}, exc_val={}, exc_tb={}".format(exc_type, exc_val, exc_tb))
        pass

    def __str__(self):
        return "some"


print("Start")
with A() as a:
    print(a)
print("End")