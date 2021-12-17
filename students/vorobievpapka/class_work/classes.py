class User:
    nick_name: str
    import time

    def __init__(self, user_name, server):
        self.nick_name = user_name
        self.server = server

    def login(self):
        self.server.login_user()

    def logout(self):
        pass

    def send_message(self, text):
        self.server.get_message(
            {
                "user_name": self.nick_name,
                "text": text
             }

        )

    def get_message_list(self, is_print=False):
        if is_print:
            for i in self.server.send_message_list():
                print(i)
        else:
            return self.server.send_message_list()

class Server:
    message_list: list
    import time
    def __init__(self):
        self.message_list = list()

    def login_user(self):
        return True

    def send_message_list(self):
        return self.message_list

    def get_message(self, text):
        text["time"] = self.time.time()
        self.message_list.append(text)
