from dec_logg import timeit

class User:
 
    @timeit
    def user():

        name = str(input("<<< Добро пожаловать в чат >>> \n Введите ваше имя> "))
        message = str(input("<<< Введите ваше сообщение > "))
        message_result = {name:message}
        return message_result
    
    @timeit
    def user1():
        hoo= str(input("Введите имя того кому хотите отправить сообщение > "))
        print("Ваше сообщение отправлено для ", hoo)
        return hoo

    


if __name__=="__main__":
    User.user()
    User.user1()