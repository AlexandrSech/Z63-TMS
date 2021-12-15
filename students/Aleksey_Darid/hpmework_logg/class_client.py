


def user():
    name = str(input("<<< Добро пожаловать в чат >>> \n Введите ваше имя> "))
    message = str(input("<<< Введите ваше сообщение > "))
    message_result = {name:message}
    return message_result
