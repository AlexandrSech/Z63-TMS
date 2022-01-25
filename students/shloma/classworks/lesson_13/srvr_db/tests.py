from server_classes import Server

server = Server()

t = [
    {
        "func": server.add_user,
        "tests": [
            ({"login": "123", "password": "123"}, "User '123' added to server"),
            ({"login": "123", "password": "123"}, "User with name '123' already exist"),
            ({"login": "1234", "password": ""}, "Password field empty! Please, input password"),
        ]
    }
]

if __name__ == "__main__":

    for test in t:
        for ind, test_obj in enumerate(test["tests"]):
            res = test["func"](test_obj[0])

            if res == test_obj[1]:
                print(f"Test #{ind}: Test completed")
            else:
                print(f"Test #{ind}: Test fault! Await: '{test_obj[1]}', got: '{res}'")


