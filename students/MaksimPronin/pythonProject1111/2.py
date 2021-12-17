import logging


class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)

        handler = self.get_handler()
        self.logger.addHandler(handler)

    def get_handler(self):
        handler = logging.FileHandler('log.txt')
        handler.setLevel(logging.INFO)
        log_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(log_format)
        return handler


logger = Logger().logger


class User:

    def __init__(self, username: str):
        self.username = username


class Chat:

    def __init__(self, name: str):
        self.name = name
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)

    def send_message(self, user, message):
        if user in self.users:
            self.messages = "{username}: {message}".format(
                username=user.username,
                message=message,
            )
            logger.info('sdafasdf')
        else:
            logger.error("Unaoth")

    def __repr__(self):
        return str(self.users)


logger.info('sdafasdf')

max = User(username="max")
roma = User(username="roma")

chat1 = Chat(name="pidory")

chat1.join(max)
#chat1.join(roma)
chat1.send_message(max, 'hello')
chat1.send_message(roma, 'hello')

print(roma)
print(chat1)
print(chat1.users)
print(chat1.messages)