# 2022-01-14
# shlom41k


from flask import Flask, request

from server_classes import Server


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/login", methods=["POST"])
def login():
    return str(server.check_user(request.json))


@app.route("/message", methods=["GET", "POST"])
def message():
    if request.method == "GET":
        return str({"message": {"user": "", "text": ""}, "token": ""}).replace("'", "\"")
    elif request.method == "POST":
        server.get_message(request.json["message"], request.json["token"])
        return "Message sent to server"


@app.route("/message_list", methods=["GET"])
def message_list():
    ans = server.send_list(request.json["token"])
    return str(ans) if ans is not None else "Unknown user"


if __name__ == "__main__":
    server = Server()
    app.run(debug=True)