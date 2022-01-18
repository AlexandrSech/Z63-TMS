from time import time

CLIENT_LIST = [
    {"login": "user1", "password": "12345"},
    {"login": "root", "password": "root"},
    {"login": "user2", "password": "1111"},
    {"login": "alex", "password": "42"},
]


class Auth:
    def __init__(self):
        self.token_list = []
        self.token_format = {"user": {}, "token": ""}

    def check_user(self, creds: dict):
        if creds in CLIENT_LIST:
            return self.add_user(creds)
        return False

    def generate_token(self):
        return str(time())

    def add_user(self, creds: dict):
        token = self.generate_token()
        self.token_format["user"] = creds
        self.token_format["token"] = token
        self.token_list.append(self.token_format)
        return token


class Chat:
    def __init__(self):
        self.message_list = []

    def get_message(self, text, token):
        self.message_list.append(text)

    def send_list(self, token):
        return self.message_list


class Server(Auth, Chat):
    def __init__(self):
        Auth.__init__(self)
        Chat.__init__(self)

    def check_token(self, token):
        check = False
        for i in self.token_list:
            if i["token"] == token:
                check = True
        return check

    def get_message(self, text, token):
        if self.check_token(token):
            self.message_list.append(text)

    def send_list(self, token):
        if self.check_token(token):
            return self.message_list


if __name__ == '__main__':
    auth = Auth()
    tests = [
        {"func": auth.check_user, "tests":
            [
                [{"login": "user1", "password": "12345"}, time],
                [{"login": "user5", "password": "12345"}, False],
                [{}, False],
                [{"login": "user5"}, False],
                [1233456784, False],
                ["1233456784", False],
            ]},
    ]

    for func in tests:
        for test in func["tests"]:
            result = func["func"](test[0])
            print(f"test for func {func['func']}")
            print(f"args {test[0]}")
            print(f"result {result}")
            print(f"result {test[1]}")
            print(result == test[1])
            print()
