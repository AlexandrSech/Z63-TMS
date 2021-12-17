from classes import User, Server









server = Server()


users_list = []
for i in range(5):
    users_list.append(User(str(i), server))

for user in users_list:
    user.send_message("sfdsefvsdfvsav " + user.nick_name)
    user.get_message_list(is_print=True)
    print()






