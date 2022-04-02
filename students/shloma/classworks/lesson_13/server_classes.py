# shlom41k

from secrets import token_hex


class Users:
    __users: list

    def __init__(self):

        self.__users = []
        # user = {"login": "user", "password": "root"}

    @property
    def users(self):
        return self.__users

    def add(self, user: dict):
        self.__users.append(user)

    def remove(self, user: dict):
        self.__users.remove(user)


class Chat:
    __messages: list

    def __init__(self):
        self.__messages = []
        # message = "datetime + <user> + text"

    @property
    def messages(self):
        return self.__messages

    def add_message(self, message: str):
        self.__messages.append(message)

    def __clear_history(self):
        self.__messages = []


class Session:
    __tokens = []
    # token = {"login": "", "token": ""}

    def __init__(self):
        self.__tokens = []

    @property
    def tokens(self):
        return self.__tokens

    def add(self, token: dict):
        self.__tokens.append(token)

    def remove(self, token):
        self.__tokens.remove(token)


class Server:

    _users: Users
    _chat: Chat
    _session: Session

    def __init__(self):
        self._users = Users()
        self._chat = Chat()
        self._session = Session()

    @property
    def users(self):
        return self._users.users

    @property
    def messages(self):
        return self._chat.messages

    def add_user(self, user: dict):
        # add user to users list

        try:
            is_exist, message = self.check_user(user, login_only=True)
            if is_exist:
                return message
            if not user['password']:
                return f"Password field empty! Please, input password"

            self._users.add(user)
            return f"User '{user['login']}' added to server"
        except:
            raise ValueError

    def check_user(self, user: dict, login_only=False):
        # check user in user list

        message = ""

        for server_user in self._users.users:
            if server_user["login"] == user["login"]:
                if login_only:
                    message = f"User with name '{user['login']}' already exist"
                    return True, message

                if server_user["password"] == user["password"]:
                    message = "Validation success"
                    return True, message
                else:
                    message = "Uncorrected password"
                    return False, message
        else:
            message = f"Unknown user '{user['login']}'. Register at first!"
            return False, message

    def login(self, user: dict):
        # authorize user in current session

        is_exist, message = self.check_user(user)

        if is_exist:
            return self.__get_token(user)

        return message

    def __get_token(self, user: dict):
        # search token in session list, or generate new

        for user_token in self._session.tokens:
            if user["login"] == user_token["login"]:
                return user_token

        token = {"login": user["login"], "token": self.__generate_token()}
        self._session.add(token)
        return token

    def __generate_token(self):
        # generate token

        return token_hex()

    def check_token(self, user: dict):
        # search token in session list

        if user in self._session.tokens:
            return True
        return False

    def logout(self, user: dict):
        # remove user from current session

        if user not in self._session.tokens:
            return f"User '{user['login']}' unauthorized!"
        try:
            self._session.remove(user)
        except:
            pass
        return f"User '{user['login']}' logout"

    def get_message_from_user(self, message: dict):
        # get message from user and add into a messages list

        if not self.check_token(message["user"]):
            return f"Unauthorized user! Login at first"

        mes = f"{message['message']['datetime']} <{message['user']['login']}>: {message['message']['text']}"
        self._chat.add_message(mes)
        return f"Message sent to chat"

    def send_messages_list(self, user: dict):
        # send chat history to user

        if not self.check_token(user):
            return f"Unauthorized user! Login at first"

        chat_history = "\n".join(self._chat.messages)

        return chat_history if chat_history else "No chat history"


if __name__ == "__main__":

    s = Server()
    print(s.users)
    print(s.check_user({"login": "user", "password": "123"}, login_only=True))
    print(s.add_user({"login": "user5", "password": "123"}))
    print(s.users)
    print(s.messages)
    print(s.login({"login": "user54", "password": "123"}))
