class User:
    nick_name: str

    def __init__(self, user_name, server):
        self.nick_name = user_name
        self.server = server

    def send_message(self, text):
        self.server.get_message_from_user(text)

    def get_message_list(self, is_print=False):
        return self.server.send_message_list()


class Server:
    import time

    message_list: list

    def __init__(self):
        self.message_list = list()

    def login_user(self):
        return True

    def send_message_list(self):
        return self.message_list

    def get_message_from_user(self, text):
        self.message_list.append(text)
