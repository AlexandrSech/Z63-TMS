# -*- coding: utf-8 -*-

"""
Class "Client" for my server chat.
Client have chat nickname and date of registration
Client can:
    --> send message to chat
    --> get message from chat
    --> get chat history
    --> get chat status
"""

from requests.exceptions import HTTPError
from datetime import datetime
import requests
import json

from settings import SERVER, API_SERVER_STATUS, API_HISTORY, API_MESSENGER


class Client:

    __nick_name: str
    __date_of_reg: datetime

    def __init__(self, nick_name: str):
        self.__nick_name = nick_name
        self.__date_of_reg = datetime.now()

    def __str__(self):
        return self.__nick_name

    @property
    def nick_name(self):
        return self.__nick_name

    @nick_name.setter
    def nick_name(self, nick_name: str):
        self.__nick_name = nick_name

    @property
    def date_of_reg(self):
        return self.__date_of_reg

    def send_message(self, message: str):
        url = SERVER + API_MESSENGER
        msg = '{{"UserName": "{}", "MessageText": "{}", "TimeStamp": "{}"}}'.format(self.nick_name, message, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(f"Отправлено сообщение: {msg}")

        data = json.loads(msg)
        r = requests.post(url, json=data)   # seng message
        return f"Status code: {r.status_code}, reason: {r.reason}"

    @staticmethod
    def get_request(url: str):
        try:
            response = requests.get(url)
            # If Successful, do not raise errors
            response.raise_for_status()
        except HTTPError as http_err:       # HTTP error
            return None
        except Exception as err:            # other error
            return None
        else:
            return response

    def get_message(self, id: int):
        url = SERVER + API_MESSENGER + "/" + str(id)
        response = self.get_request(url)

        if response is not None:
            text = response.json()
            return f"ID={id}: {text['TimeStamp']}: <{text['UserName']}>: {text['MessageText']}"
        else:
            print("ERROR: NO answer from server")

    def get_history(self):
        url = SERVER + API_HISTORY
        response = self.get_request(url)

        if response is not None:
            return response.json()
        else:
            print("ERROR: NO answer from server")

    def print_history(self):
        hist = self.get_history()
        for key in sorted(hist.keys(), key=int):
            print(f"ID={int(key)}: {hist[key]}")

    def get_status(self):
        url = SERVER + API_SERVER_STATUS
        response = self.get_request(url)

        if response is not None:
            return f"Server status: {response.json()}"
        else:
            print("ERROR: NO answer from server")


if __name__ == "__main__":

    s1 = Client("shlom41k")
    print(s1.date_of_reg)
    s1.send_message("loooooooool")
    print(s1.send_message("kekekeke"))
    print(s1.send_message("fkjsdgfsdjhfds"))
    print(s1.send_message("sdfsdfsdf"))
    print(s1.get_message(1))

    # h = s1.get_history()
    #
    # for key in sorted(h.keys(), key=int):
    #     print(f"ID={int(key)}: {h[key]}")

    s1.print_history()

    print(s1.get_status())



