from flask import Flask, request
from data_classes import Users, Session

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def print_data():
    print(users.users)
    print(session.session)


@app.route("/create_user", methods=["POST"])
def create_user():
    print_data()
    return users.create_user(request.json["login"], request.json["password"])


@app.route("/login", methods=["POST"])
def login():
    response = users.check_user(request.json["login"], request.json["password"])
    if not response[1]:
        return response[0]
    session.add(response[0])
    print_data()
    return response[0]


@app.route("/logout", methods=["POST"])
def logout():
    # {"token": tsdjnvaknsfd}
    token = request.json["token"]
    session.remove(token)
    print_data()
    return "Logout OK!"


if __name__ == '__main__':
    users = Users()
    session = Session()
    app.run(debug=True)
