

class Users:
    def __init__(self):
        self.users = list()

    def create_user(self, login, password):
        if self.check_user(login, password)[1]:
            return "Current user already exist!"
        self.users.append(
            {"login": login, "password": password}
        )
        return "User created."

    def check_user(self, login, password):
        '''if self_use:
            return any([True if login in user.values() else False for user in self.users])
        else:'''
        for user in self.users:
            if user["login"] == login:
                if user["password"] == password:
                    return "token", True
                else:
                    return "Wrong password", False
            else:
                return "Unknown login", False
        return "", False


class Session:
    def __init__(self):
        self.session = list()

    def add(self, token):
        self.session.append(token)

    def remove(self, token):
        self.session.remove(token)


if __name__ == '__main__':
    s = Session()
    s.add("sdfb")
    s.remove("sdfb")

    """u = Users()
    r = u.create_user("test1", "adsfgsd")
    print(r)"""

