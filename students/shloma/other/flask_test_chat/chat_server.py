from flask import Flask, request
from settings import API_SERVER_STATUS, API_MESSENGER, API_HISTORY, SERVER_LOG
from datetime import datetime
from logger import Logger

srv_log = Logger(SERVER_LOG)

log_template = "{}, type: {}, data: {}"
srv_log.add(log_template.format(datetime.now(), "SRV_ANSWER", "Logger started"))

app = Flask(__name__)
srv_log.add(log_template.format(datetime.now(), "SRV_ANSWER", "Server started"))

list_of_messages = []   # Список всех сообщений

@app.route("/")
def hello_world():
    srv_log.add(log_template.format(datetime.now(), request.method, request.json))
    message = "Messenger Flask server is running<br> <a href='/status'> Check status </a>"
    srv_log.add(log_template.format(datetime.now(), "SRV_ANSWER", message))
    return message


@app.route(API_SERVER_STATUS)
def status():
    srv_log.add(log_template.format(datetime.now(), request.method, request.json))
    message = {"Messages_count": len(list_of_messages)}
    srv_log.add(log_template.format(datetime.now(), "SRV_ANSWER:", message))
    return message


@app.route(API_HISTORY)
def all_messages():
    srv_log.add(log_template.format(datetime.now(), request.method, request.json))
    d = dict()
    for i, elem in enumerate(list_of_messages):
        d[f"{i}"] = f"{elem}"

    message = d, 200
    srv_log.add(log_template.format(datetime.now(), "SRV_ANSWER:", message))
    return message


@app.route(API_MESSENGER, methods=["POST"])
def send_message():
    srv_log.add(log_template.format(datetime.now(), request.method, request.json))

    msg = request.json
    list_of_messages.append(msg)

    msgtext = f"{msg['UserName']} <{msg['TimeStamp']}>: {msg['MessageText']}"
    print(f"Total messages: {len(list_of_messages)}. Sent message: {msgtext}")

    message = f"Message sent successful. Total messages: {len(list_of_messages)}", 200
    srv_log.add(log_template.format(datetime.now(), "SRV_ANSWER:", message))
    return message


@app.route(API_MESSENGER + "/<int:id>")
def get_message(id):
    srv_log.add(log_template.format(datetime.now(), request.method, request.json))
    if 0 <= id < len(list_of_messages):
        message = list_of_messages[id], 200
        srv_log.add(log_template.format(datetime.now(), "SRV_ANSWER:", message))
        return message
    else:
        message = "Not found", 400
        srv_log.add(log_template.format(datetime.now(), "SRV_ANSWER:", message))
        return message


if __name__ == '__main__':
    app.run(debug=True)
