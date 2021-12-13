def write():
    # open file
    file_stream = open("example1.txt", "w")

    # make text
    text = str()
    for i in range(100):
        text += str(i)*100 + "\n"
    # print(text)

    # write text in file
    file_stream.write(text)

    file_stream.close()


def read():
    fs = open("example1.txt", "r")
    text = fs.read()
    # print(text)
    for line in text.splitlines():
        print(line)
    fs.close()
    return text


def read_2(file_name):
    with open(file_name, "r") as fs:
        return fs.read()


def add_log(file_name, text):
    with open(file_name, "a") as fs:
        fs.write(text)


if __name__ == '__main__':
    file_name = "example1.txt"

    add_log(file_name, "some text")

    t = read_2(file_name)
    print(t)


