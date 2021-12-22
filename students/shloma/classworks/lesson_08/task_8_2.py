# 2021-12-17

from classes import User, Server

server = Server()

users_list = [User(str(i), server) for i in range(5)]

for user in users_list:
    user.send_message("" + user.nick_name)
    print(f"User {user} send message")

    user.get_message_list(is_print=True)
    print()

