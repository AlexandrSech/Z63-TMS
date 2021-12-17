from classes import User, Server


class TestUser:

    def test_init(self):
        tests = [
            ((1,1), (1,1)),
            (("name", Server), ("name", Server)),
        ]

        for test in tests:
            user = User(*test[0])
            if (user.nick_name, user.server) == test[1]:
                print("Test passed")
            else:
                print("Test error: {}".format(test))

    def test_send_message(self):
        pass


if __name__ == '__main__':
    test = TestUser()
    test.test_init()
