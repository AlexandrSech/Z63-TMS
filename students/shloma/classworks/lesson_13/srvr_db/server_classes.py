# shlom41k
from CRUD import db, CRUD
from settings import login_template, logout_template, message_template
from secrets import token_hex


class Server:

    _crud: CRUD

    def __init__(self):
        self._crud = CRUD(db)

    @property
    def users(self):
        return self._crud.get_users()

    @property
    def messages(self):
        return self._crud.get_messages()

    def add_user(self, user: dict):
        # add user to users list
        # {"login": "login", "password": "password"}

        if user.keys() != login_template.keys():
            return f"Invalid registration form!"

        try:
            is_exist, message = self.check_user(user, login_only=True)
            if is_exist:
                return message
            if not user['password']:
                return f"Password field empty! Please, input password"

            # self._db.users.append(user)
            self._crud.add_user(user["login"], user["password"])
            return f"User '{user['login']}' added to server"
        except:
            raise ValueError

    def check_user(self, user: dict, login_only=False):
        # check user in user list
        message = ""

        for server_user in self._crud.get_users():
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

        if user.keys() != login_template.keys():
            return f"Invalid registration form!"

        is_exist, message = self.check_user(user)

        if is_exist:
            return self.__get_token(user)

        return message

    def __get_token(self, user: dict):
        # search token in session list, or generate new

        for user_token in self._crud.get_tokens():
            if user["login"] == user_token["login"]:
                return user_token

        # token = {"login": user["login"], "token": self.__generate_token()}
        # self._session.add(token)
        token = self.__generate_token()
        self._crud.add_token(user["login"], token)
        return {"login": user["login"], "token": token}

    def __generate_token(self):
        # generate token
        return token_hex()

    def check_token(self, user: dict):
        # search token in session list

        if user in self._crud.get_tokens():
            return True
        return False

    def logout(self, user: dict):
        # remove user from current session

        if user.keys() != logout_template.keys():
            return f"Invalid logout form!"

        if user not in self._crud.get_tokens():
            return f"User '{user['login']}' unauthorized!"
        try:
            self._crud.remove_token(user["login"], user["token"])
        except:
            pass
        return f"User '{user['login']}' logout"

    def get_message_from_user(self, message: dict):
        # get message from user and add into a messages list

        if message.keys() != message_template.keys():
            return f"Invalid message form!"

        if not self.check_token(message["user"]):
            return f"Unauthorized user! Login at first"

        self._crud.add_message(date=message['message']['datetime'],
                               login=message['user']['login'],
                               text=message['message']['text'])
        return f"Message sent to chat"

    def send_messages_list(self, user: dict):
        # send chat history to user

        if user.keys() != logout_template.keys():
            return f"Invalid request form!"

        if not self.check_token(user):
            return f"Unauthorized user! Login at first"

        chat_history = "\n".join(self._crud.get_messages())

        return chat_history if chat_history else "No chat history"


if __name__ == "__main__":

    s = Server()
    print(s.users)
    print(s.check_user({"login": "user", "password": "123"}, login_only=True))
    print(s.add_user({"login": "user5", "password": "123"}))
    print(s.users)
    print(s.messages)
    print(s.login({"login": "user54", "password": "123"}))
