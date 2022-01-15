# 2022-01-14
# shlom41k

from server_classes import Auth, Server

auth = Auth()
s1 = Server()

tests = [
    {"func": auth.check_user, "tests":
        [
            [{"login": "user", "password": "12345"}, time],
            [{"login": "user5", "password": "12345"}, False],
            [{}, False],
            [{"login": "user5"}, False],
            [124234234234, False],
            ["124234234234", False],
        ]},
]


if __name__ == "__main__":
    for func in tests:
        for test in func["tests"]:
            result = func["func"](test[0])
            print(f"Test for func '{func}'")
            print(f"Args={test[0]}")
            print(f"Result = {result}, available result={test[1]}")
            print(True if result == test[1] else False)
            print()
