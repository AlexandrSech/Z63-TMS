from models import User, Token, Message, DataBase


db = DataBase()   # Create database


class CRUD:

    def __init__(self, database: DataBase):
        self._db = database

    def change_db(self, database: DataBase):
        self._db = database

    def add_user(self, login: str, password: str):
        self._db.users.append(User(login, password))

    def get_users(self):
        # {"login": "", "password": ""}
        return [{"login": user.login, "password": user.password} for user in self._db.users]

    def add_token(self, login: str, token: str):
        self._db.session.append(Token(login, token))

    def get_tokens(self):
        # {"login": "", "token": ""}
        return [{"login": user.login, "token": user.token} for user in self._db.session]

    def remove_token(self, login: str, token: str):
        for auth_token in self._db.session:
            if auth_token.login == login and auth_token.token == token:
                self._db.session.remove(auth_token)

    def add_message(self, date: str, login: str, text: str):
        self._db.messages.append(Message(date, login, text))

    def get_messages(self):
        # "datetime <user>: text"
        return [f"{message.date} <{message.user}>: {message.text}" for message in self._db.messages]

    def get_full_messages(self):
        return [f"id={message.id}, date={message.date}, user={message.user} text={message.text}" for message in self._db.messages]


if __name__ == "__main__":
    db = DataBase()
    crud = CRUD(db)

    print(crud.get_users())

    crud.add_user("ksdjhf", "ksdjhgf")
    crud.add_user("123", "ksdj3453465hgf")
    crud.add_user("dsfs", "ksdj43566hgf")

    print(crud.get_users())

    crud.add_token("shlom41k", "skdgfsdf")
    crud.add_token("23423", "skjdhf")
    crud.add_token("erte", "skdgf")

    print(crud.get_tokens())

    crud.add_message("sdjf", "kdasf", "gddddddddddddd")
    crud.add_message("sdjf", "kdasf", "gddddddddddddd")
    crud.add_message("sdjf", "kdasf", "gddddddddddddd")
    crud.add_message("sdjf", "kdasf", "gddddddddddddd")

    print(crud.get_messages())
    print(crud.get_full_messages())


