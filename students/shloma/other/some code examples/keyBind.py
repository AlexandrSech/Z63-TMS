from keybind import KeyBinder
import time


class Test:
    def __init__(self, value):
        self.__value = value

    def test(self):
        print(self.__value)


t = Test("22")

KeyBinder.activate({
    "Ctrl-K": t.test,
}, run_thread=True)


while True:
    print(3)
    time.sleep(1)
