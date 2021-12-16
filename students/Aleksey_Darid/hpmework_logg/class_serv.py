from os import name
import class_client
from dec_logg import timeit

users = []
messages = {}
@timeit
def serv():
    messages.update(class_client.User.user())
    users.append(class_client.User.user1())
    print(users, messages)


def send_m():
    



if __name__=="__main__":
    serv()   
    send_m()