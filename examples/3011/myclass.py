class A:
    n: float

    def set_n(self, value=None):
        if value == None:
            return
        elif type(value) == float:
            self.n = value
        elif type(value) != float:
            if type(value) in [int, bool, str]:
                if type(value) == str:
                    temp = self.check_str(value)
                else:
                    self.n = float(value)
        else:
            raise ValueError

    def check_str(self, my_str):
        check_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ]
        dot_number = 0
        for i, v in enumerate(my_str):
            print(i, v)
            if i == 0 and v == "-":
                continue
            elif v in check_list:
                if v == ".":
                    dot_number += 1
                if dot_number > 1:
                    return False
            else:
                return False
        else:
            return True


a = A()

r = a.check_str("-.17")
print(r)

exit()


tests = [
    {"input_value": 1, "result_value": 1},
    {"input_value": 1, "result_value": 1},
    {"input_value": 1, "result_value": 1},
    {"input_value": 1, "result_value": 1},
    {"input_value": 1, "result_value": 1},
]

for test in tests:
    a = A()
    a.set_n(test["input_value"])
    if a.n != test["result_value"]:
        print("Test failed")
    else:
        print("Test failed")
