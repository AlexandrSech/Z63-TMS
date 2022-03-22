from dataclasses import dataclass, field


"""
@dataclass(frozen=True)
class Message:
    date: str
    user: str
    text: str
"""


@dataclass(frozen=True)
class User:
    login: str
    password: str


@dataclass(frozen=True)
class Token:
    login: str
    token: str


class Message:
    id: int = 0

    def __init__(self, date: str, user: str, text: str):
        self.date = date
        self.user = user
        self.text = text

        self.id = self.__class__.id
        self.__class__.id += 1

    def __del__(self):
        if self.id == self.__class__.id - 1:
            self.__class__.id -= 1

    def __repr__(self):
        return f"{self.date} <{self.user}>: {self.text}"


@dataclass
class DataBase:
    users: list[User] = field(default_factory=list)
    session: list[Token] = field(default_factory=list)
    messages: list[Message] = field(default_factory=list)


if __name__ == "__main__":
    db = DataBase()         # Создание условной базы данных (БД)
    db.users.append(User("user", "root"))    # Добавление нового пользователя в БД
    db.session.append(Token("user", "sdfg8d5f6gd8f9g"))    # Добавление пользователя в сессию
    db.messages.append(Message("2022-01-21 07:22:12", "user", "Hello, world"))  # Добавление сообщения в БД
