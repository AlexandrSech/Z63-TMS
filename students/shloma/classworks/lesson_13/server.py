from flask import Flask, request
from settings import URL_ADD_USER, URL_LOGIN, URL_LOGOUT, URL_MESSAGE, URL_MESSAGES
from settings import login_template, logout_template, message_template
from server_classes import Server


server = Server()
app = Flask(__name__)


# /127.0.0.1:5000
@app.route("/")
def hello():
    return "Welcome in my_simple_chat"


# /add_user
@app.route(URL_ADD_USER, methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return login_template
        # return str(login_template).replace("'", '"')

    elif request.method == "POST":
        try:
            ans = server.add_user(request.json)
        except:
            ans = "ERROR: Bad request from user"
        return ans


# /login
@app.route(URL_LOGIN, methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return login_template

    elif request.method == "POST":
        try:
            ans = server.login(request.json)
        except:
            ans = "ERROR: Bad request from user"
        return ans


# /logout
@app.route(URL_LOGOUT, methods=["GET", "POST"])
def logout():
    if request.method == "GET":
        return logout_template

    elif request.method == "POST":
        try:
            ans = server.logout(request.json)
        except:
            ans = "ERROR: Bad request from user"
        return ans


# /get message from user
@app.route(URL_MESSAGE, methods=["GET", "POST"])
def message():
    if request.method == "GET":
        return message_template

    elif request.method == "POST":
        try:
            ans = server.get_message_from_user(request.json)
        except:
            ans = "ERROR: Bad request from user"
        return ans


# /sedd messages list to user
@app.route(URL_MESSAGES)
def messages():
        try:
            ans = server.send_messages_list(request.json)
        except:
            ans = "ERROR: Bad request from user"
        return ans


if __name__ == "__main__":
    app.run(debug=True)