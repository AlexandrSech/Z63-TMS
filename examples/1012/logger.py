class logger:
    _file_name: str

    def __init__(self, file_name):
        print("init")
        self.change_file(file_name)

    def add(self, text):
        with open(self._file_name, "a") as fs:
            fs.write(text + "\n")

    def read(self):
        with open(self._file_name, "r") as fs:
            return fs.read()

    def change_file(self, file_name):
        self._file_name = file_name


l = logger("log1.log")

print(l.read())
l.add("123")
print(l.read())
l.add("456")
print(l.read())
l.add("789")
print(l.read())

l.change_file("log2.log")

print(l.read())
l.add("123")
print(l.read())
l.add("456")
print(l.read())
l.add("789")
print(l.read())


