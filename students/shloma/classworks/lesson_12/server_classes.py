# 2022-01-14
# shlom41k


from time import time


CLIENT_LIST = [
    {"login": "user", "password": "12345"},
    {"login": "root", "password": "root"},
    {"login": "user2", "password": "11111"},
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

    @staticmethod
    def generate_token():
        token = str(time())
        return token

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

    def get_message(self, text, token):
        if self.check_token(token):
            self.message_list.append(text)
            return True
        return False

    def send_list(self, token):
        if self.check_token(token):
            return self.message_list

    def check_token(self, token):
        check = False
        for i in self.token_list:
            if i["token"] == token:
                check = True
        return check

    def delete_user(self, token):
        for user in self.token_list:
            if user["token"] == token:
                self.token_list.remove(user)
                return True

        return False


if __name__ == "__main__":

    s1 = Server()
    print(s1.generate_token())

