import sys
import datetime
import json
import requests
from requests.exceptions import HTTPError
from PyQt6 import uic, QtCore, QtGui, QtWidgets

LOCAL_HOST = "http://127.0.0.1:5000"
API_MESSENGER = "/api/Messenger"
UI_FILE = "messenger.ui"


class MainWindow(QtWidgets.QMainWindow):
    server_adress = LOCAL_HOST
    message_id = 0

    def __init__(self, *args, **kwargs):
        # Вызовем метод унаследованных классов __init__ method
        super(MainWindow, self).__init__(*args, **kwargs)

        # Загрузим файл .ui
        uic.loadUi(UI_FILE, self)

        # Обработчик события нажатия кнопки
        self.pushButton1.clicked.connect(self.pushButton_clicked)

    def pushButton_clicked(self):
        self.send_message()

    def send_message(self):
        user_name = self.lineEdit1.text()
        message_text = self.lineEdit2.text()
        time_stamp = str(datetime.datetime.now())
        msg = f"{{\"UserName\": \"{user_name}\", \"MessageText\": \"{message_text}\", \"TimeStamp\": \"{time_stamp}\"}}"
        url = self.server_adress + API_MESSENGER
        data = json.loads(msg)
        r = requests.post(url, json=data)
        print(f"Отправлено сообщение: {msg}")
        print(r.request.body)
        # print(f"Status code: {r.status_code}, reason: {r.reason}")

    def get_message(self, id: int):
        url = self.server_adress + API_MESSENGER + "/" + str(id)
        print(url)

        try:
            response = requests.get(url)

            # If Successful, do not raise errors
            response.raise_for_status()
        except HTTPError as http_err:
            # HTTP error
            return None
        except Exception as err:
            # other error
            return None
        else:
            text = response.text
            return text

    def timer_event(self):
        msg = self.get_message(self.message_id)
        while msg is not None:
            msg = json.loads(msg)
            user_name = msg["UserName"]
            message_text = msg["MessageText"]
            time_stamp = msg["TimeStamp"]
            msg_text = f"{time_stamp} : <{user_name}> : {message_text}"
            print(msg_text)
            self.listWidget1.insertItem(self.message_id, msg_text)
            self.message_id += 1
            msg = self.get_message(self.message_id)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    timer = QtCore.QTimer()
    time = QtCore.QTime(0, 0, 0)
    timer.timeout.connect(w.timer_event)
    timer.start(5000)
    sys.exit(app.exec())

