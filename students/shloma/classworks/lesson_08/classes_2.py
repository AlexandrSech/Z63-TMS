class User:
    import requests

    nick_name: str

    def __init__(self, user_name, server):
        self.nick_name = user_name
        self.server = server

    def __str__(self):
        return self.nick_name

    def login(self):
        pass

    def logout(self):
       pass

    def send_message(self, text):
        self.server.get_message_from_user(text)

    def get_message_list(self):
        return self.server.send_message_list()


class Server:
    from time import time

    message_list: list

    def __init__(self):
        self.message_list = list()

    def login_user(self):
        pass

    def send_message_list(self):
        return self.message_list

    def get_message_from_user(self, text):
        self.message_list.append(text)


if __name__ == "__main__":

    server = Server()

    u1 = User("1", server)
    u1.send_message("Hello")
    print(u1.get_message_list())

