from loguru import logger

class User:
 
    @logger.catch
    def user():

        name = str(input("<<< Добро пожаловать в чат >>> \n Введите ваше имя> "))
        hoo= str(input("Введите имя того кому хотите отправить сообщение > "))
        message = str(input("<<< Введите ваше сообщение > "))
        print("Ваше сообщение отправлено для ", hoo)
        message_result = {name:message}
        return message_result, hoo
    
    #@logger.catch
    #def user1():
        #hoo= str(input("Введите имя того кому хотите отправить сообщение > "))
        #print("Ваше сообщение отправлено для ", hoo)
        #return hoo

    


if __name__=="__main__":
    User.user()
   