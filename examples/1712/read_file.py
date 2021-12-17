class User:
    name: str
    email: str
    password: str
    other: str

    def __init__(self, name, email, password, other=""):
        self.name = name
        self.email = email
        self.password = password
        self.other = other

    def get_data(self):
        return {
            "name": self.name, "email": self.email, "pass": self.password, "other": self.other
        }



class A:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        # read
        text = str()
        with open(self.file_name, "r") as f:
            text = f.read()
        self.text = text

    def parce(self):
        # parce text
        data = []

        for line in self.text.splitlines():
            u = User(*line.split("|"))


            '''templ = {"name": str(), "email": str(), "pass": str(), "other": ""}
            keys = tuple(templ.keys())

            for index, value in enumerate(line.split("|")):
                if index >= len(keys):
                    templ["other"] += value + " "
                else:
                    templ[keys[index]] = value'''

            data.append(u)
        self.data = data

    def print_all(self):
        # print
        for user in self.data:
            for key, value in user.get_data().items():
                print("{key}: {val}".format(key=key, val=value))
            print()


if __name__ == '__main__':
    a = A("file.txt")
    a.read()
    a.parce()
    a.print_all()

