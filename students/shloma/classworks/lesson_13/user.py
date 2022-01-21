# shlom41k

import requests
from datetime import datetime
from settings import URL_SERVER, URL_LOGIN, URL_LOGOUT, URL_ADD_USER, URL_MESSAGE, URL_MESSAGES


class User:

    _login: str
    _password: str
    _token: str

    _login_form: dict
    _logout_form: dict

    _message_form: dict

    def __init__(self, login: str, password: str):
        self._login = login
        self._password = password
        self._token = ""

        self._login_form: dict = {}
        self._logout_form: dict = {}
        self._message_form: dict = {}

    def __repr__(self):
        return f"User: login='{self._login}', password='{self._password}'"

    def __call__(self, message: str):
        return self.send_message(message)

    def get_login_form(self, token=False):
        self._login_form = requests.get(URL_SERVER + (URL_LOGIN if token else URL_ADD_USER)).json()

    def get_logout_form(self):
        self._logout_form = requests.get(URL_SERVER + URL_LOGOUT).json()

    def get_message_form(self):
        self._message_form = requests.get(URL_SERVER + URL_MESSAGE).json()

    def connect_to_server(self, token=False):
        state = False

        if self._login_form == {}:
            try:
                self.get_login_form(token)
            except:
                return state, f"ERROR: Bad answer from server"

        try:
            self._login_form["login"] = self._login
            self._login_form["password"] = self._password
        except:
            return state, f"ERROR: Invalid register form"

        try:
            ans = requests.post(URL_SERVER + (URL_LOGIN if token else URL_ADD_USER), json=self._login_form)
            state = True
        except:
            return state, f"ERROR: Bad answer from server"

        ans = ans.json() if token else ans.text

        return (state, ans) if token else ans

    def login_to_server(self):
        state, message = self.connect_to_server(token=True)

        if state:
            self._token = message["token"]
            return f"Authorization successful"

        return message

    def logout_from_server(self):
        if self._logout_form == {}:
            try:
                self.get_logout_form()
            except:
                return f"ERROR: Bad answer from server"

        try:
            self._logout_form["login"] = self._login
            self._logout_form["token"] = self._token
        except:
            return f"ERROR: Invalid logout form"

        try:
            ans = requests.post(URL_SERVER + URL_LOGOUT, json=self._logout_form).text
        except:
            return f"ERROR: Bad answer from server"

        return ans

    def send_message(self, message_text: str):
        # message_form = {"user": {"login": "", "token": ""}, "message": {"datetime": "", "text": ""}}

        if not isinstance(message_text, str):
            return f"ERROR: Message must be 'str' type!"

        if self._message_form == {}:
            try:
                self.get_message_form()
            except:
                return f"ERROR: Bad answer from server"

        try:
            self._message_form["user"]["login"] = self._login
            self._message_form["user"]["token"] = self._token
            self._message_form["message"]["datetime"] = self.get_time()
            self._message_form["message"]["text"] = str(message_text)
        except:
            return f"ERROR: Invalid register form"

        try:
            ans = requests.post(URL_SERVER + URL_MESSAGE, json=self._message_form).text
        except:
            return f"ERROR: Bad answer from server"

        return ans

    @staticmethod
    def get_time():
        return datetime.strftime(datetime.now(), "%y-%m-%d %H:%M:%S")

    def get_message_list(self):
        if self._logout_form == {}:
            try:
                self.get_logout_form()
            except:
                return f"ERROR: Bad answer from server"

        try:
            self._logout_form["login"], self._logout_form["token"] = self._login, self._token
        except:
            return f"ERROR: Invalid request form"

        try:
            ans = requests.get(URL_SERVER + URL_MESSAGES, json=self._logout_form).text
        except:
            return f"ERROR: Bad answer from server"

        return ans


if __name__ == "__main__":
    u = User("user2", "12345")
    print(u.connect_to_server())
    print(u.connect_to_server())
    print(u.login_to_server())
    print(u.login_to_server())
    print(u.login_to_server())
    print(u.logout_from_server())
    print(u.logout_from_server())
    print(u.logout_from_server())
    print(u.send_message("Hello, pipl"))
    print(u.login_to_server())
    print(u("Aaaaaaaaaaaaa"))
    print(u("dfjhgdpfkgh"))
    print(u.get_message_list())
