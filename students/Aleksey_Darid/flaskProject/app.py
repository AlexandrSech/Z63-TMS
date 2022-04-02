from flask import Flask, request
from classes import Server

app = Flask(__name__)


@app.route('/')
def hello_world():  # просто дом страница
    return 'Hello World!'


@app.route('/login')
def login():  # вход в систему
    Server.login(request.json["login"], request.json["password"])
    return "Added"


@app.route('/logout')
def logout():  # выход из системы
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
