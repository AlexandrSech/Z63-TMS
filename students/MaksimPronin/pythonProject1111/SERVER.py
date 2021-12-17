import logging


class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        handler = self.get_handler()
        self.logger.addHandler(handler)

    def get_handler(self):
        handler = logging.FileHandler('log2.txt')
        handler.setLevel(logging.DEBUG)
        log_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(log_format)
        return handler


logger = Logger().logger



class User:

    def __init__(self, username: str):
        self.username = username


class Server:
    def __init__(self, ):
        self.users = []
        self.message = []

    def join(self, user):
        self.users.append(user)

    def send_message(self, user, message):
        if user in self.users:
            self.message = "{username}: {message}".format(
                username=user.username,
                message=message,
            )
            logger.info(' message send suck')
        else:
            logger.error("fuck yourself and die")


logger = Logger().logger


stalin = User(username="Iosif")

chat = Server()
chat.join(stalin)
chat.send_message(stalin, "go_fuck_yourself")

print(stalin)
print(chat)
print(chat.users)
print(chat.message)
