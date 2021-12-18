from loguru import logger
import class_client
users_m = []


@logger.catch
def serv():
    users_m.append(class_client.User.user())
    print(users_m)


def send_m():
    pass



if __name__=="__main__":
    serv()   
    send_m()