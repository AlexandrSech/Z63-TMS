# shlom41k

# URLs addresses
URL_SERVER = "http://127.0.0.1:5000/"

URL_ADD_USER = "/add_user"

URL_LOGIN = "/login"
URL_LOGOUT = "/logout"

URL_MESSAGE = "/message"
URL_MESSAGES = "/messages"


# Messages templates
login_template = {"login": "", "password": ""}
logout_template = {"login": "", "token": ""}

message_template = {
    "user": {"login": "", "token": ""},
    "message": {"datetime": "", "text": ""},
}
