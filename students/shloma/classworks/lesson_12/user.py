# 2022-01-14
# shlom41k


import requests


url = "http://127.0.0.1:5000/"
url_login = url + "login"
url_logout = url + "logout"
url_message = url + "message"
url_message_list = url + "message_list"


class User:

    _login: str
    _password: str
    _token: str

    _message_format: str = ""

    def __init__(self, login: str = "login", password: str = "password"):
        self._login = login
        self._password = password

    def __call__(self, message: str):
        self.send_message(message_text=message)

    def login_to_server(self):
        """
        # Регистрация на сервере
        """
        r = requests.post(url_login, json={"login": self._login, "password": self._password})
        self._token = r.text

    def logout_from_server(self):
        """
        # Выход из аккаунта на сервере
        """
        r = requests.get(url_logout, json={"token": self._token})
        self._token = ""
        return r.text

    def get_message(self):
        """
        # Получение от сервера шаблона для сообщений
        """
        r = requests.get(url_message)
        self._message_format = r.json()

    def send_message(self, message_text: str = "Hello"):
        """
        # Отправка сообщения на сервер
        """
        self._message_format["message"]["user"] = self._login
        self._message_format["message"]["text"] = message_text
        self._message_format["token"] = self._token
        r = requests.post(url_message, json=self._message_format)
        return r.text

    def get_messages_list(self):
        """
        # Получение от сервера списка всех сообщений
        """
        r = requests.get(url_message_list, json={"token": self._token})
        return r.text

    @property
    def login(self):
        return self._login

    @property
    def token(self):
        return self._token

    @property
    def message_format(self):
        return self._message_format if self._message_format else "No data about message format :("


if __name__ == "__main__":

    user_list = {"login": "user", "password": "12345"}

    user1 = User(login=user_list["login"], password=user_list["password"])
    user1.login_to_server()
    print(user1.token)
    user1.get_message()
    print(user1.message_format)
    print(user1.send_message("Bla bla bla"))
    print(user1.get_messages_list())
    user1("Assssssssssssaaaaaaaa")
    user1("Assssssssssssaaaaaaaa")
    print(user1.get_messages_list())
    print(user1.logout_from_server())
    print(user1.logout_from_server())
    print(user1.send_message("Bla bla bla"))


"""
# # login
# response = requests.post(url + "login", json={"login": "user", "password": "12345"})
# print(response, response.text)
#
# token = response.text
#
# response = requests.get(url + "message")
# print(response.text)
#
# m_format = response.json()
#
#
# #send message
# m_format["message"] = "AAFDkgskjfhsdf"
# m_format["token"] = token
# response = requests.post(url + "message", json=m_format)
# print(response)
#
# response = requests.get(url + "message_list", json={"token": token})
# print(response.text)
"""
