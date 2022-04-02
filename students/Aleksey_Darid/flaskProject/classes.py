import sqlalchemy as sq

class User:
    def __init__(self):
        self.lis = Data_base()


class Server:

    def login(self, log, pas):
        Data_base.update_table(log, pas)
        return True

    def logout(self):
        pass


class Data_base:
    def __init__(self):
        self.e = sq.create_engine("sqlite:///test.db")

    def create_table(self):
        self.e.execute("""
        create table user (
        id integer primary key autoincrement,
        login varchar,
        password varchar
        )
        """)

    def update_table(self, log, pas):
        self.e.execute("""
        insert into user (login, password)
        values (str(log), str(pas))
        """)

    def take(self):
        result = self.e.execute("""select * from user""")
        for user in result:
            print(user)

    def delete_elem(self):
        self.e.execute("""
        DELETE FROM user
            WHERE id = 1;
        """)

    def delete_table(self):
        self.e.execute("""
                DROP TABLE user;
                """)


if __name__ == "__main__":
    Data_base().delete_table()
    Data_base().create_table()
    a = Server().login("Alexey", "12345")