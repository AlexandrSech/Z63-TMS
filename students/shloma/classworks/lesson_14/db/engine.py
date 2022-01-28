import sqlalchemy.exc
from sqlalchemy import create_engine


class Engine:

    db_form = "sqlite:///{}"
    # connection = None
    transaction = None

    def __init__(self, db_name: str, auto_connect: bool = True):
        self.db, self.engine, self.connection = self.init(db_name, auto_connect)

    def init(self, database: str, auto_connect: bool):
        db = self.db_form.format(database)
        engine = create_engine(db)
        connection = engine.connect() if auto_connect else None
        return db, engine, connection

    def connect_to_db(self):
        self.connection = self.engine.connect()

    def disconnect_from_db(self):
        if self.connection:
            self.connection.close()

    def change_db(self, new_db: str, auto_connect=True):
        self.disconnect_from_db()
        self.init(new_db, auto_connect)

    def start_transaction(self):
        self.transaction = self.connection.begin()

    def commit(self):
        self.transaction.commit()

    def rollback(self):
        self.transaction.rollback()

    def execute(self, command: str, auto_commit: bool = True):
        self.start_transaction()

        result = self.connection.execute(command)

        if auto_commit:
            self.commit()

        return result


class CRUD:

    create_template = [
        ("id", "integer primary key autoincrement"),
        ("name", "varchar"),
        ("field_name", "field_type"),
    ]

    def __init__(self, engine: Engine):
        self.engine = engine

    def create_table(self, table_name: str, columns: list[tuple]):
        params = ", ".join([f"{column_name} {column_type}" for column_name, column_type in columns])
        command = f"CREATE TABLE {table_name} ({params})"

        try:
            self.engine.execute(command)
            print(f"Table: '{table_name}' created successfully")
        except sqlalchemy.exc.OperationalError:
            print(f"Table: '{table_name}' already exists!")
        # except:
        #     print(f"Some unknown error. Table was not created")

    def drop_table(self, table_name: str):
        try:
            self.engine.execute(f"DROP TABLE {table_name}")
            print(f"Table: '{table_name}' deleted successfully")
        except sqlalchemy.exc.OperationalError:
            print(f"No such table: '{table_name}'")
        # except:
        #     print(f"Some unknown error")

    def alter_table(self, table_name: str, action: str, column: str, description=None):
        if action == "add":
            command = f"ALTER TABLE {table_name} ADD COLUMN {column} {description}"
            message = f"COLUMN '{column} {description}' insert into a TABLE {table_name}"
        elif action == "drop":
            command = f"ALTER TABLE {table_name} DROP COLUMN {column}"
            message = f"COLUMN '{column}' deleted from TABLE {table_name}"
        else:
            return f"Unknown operand '{action}'"

        try:
            self.engine.execute(command)
            print(message)
        except sqlalchemy.exc.OperationalError:
            print(f"ERROR: Invalid input data or column '{column}' already exists")
        # except:
        #     print(f"Some unknown error")


class Table:

    def __init__(self, engine: Engine, table_name: str, fields: tuple):
        self.engine = engine
        self.table_name = table_name
        self.fields = fields

    def select(self, fields=()):
        return list(self.engine.execute(
            f"select * from {self.table_name}" if not fields else
            f"select {', '.join(map(str, fields))} from {self.table_name}")
        )

    def update(self, field_name: str, new_value, old_name):
        self.engine.execute(
            f"UPDATE {self.table_name} "
            f"SET {field_name} = '{new_value}' "
            f"WHERE {field_name} = '{old_name}'"
        )
        print(f"Value in COLUMN '{field_name}' updated from {old_name} to {new_value}")

    def insert(self, values: tuple):
        self.engine.execute(
            f"INSERT INTO {self.table_name} ({', '.join([item for item in self.fields])}) VALUES "
            f"({', '.join([chr(39) + str(item) + chr(39) for item in values])})"
        )
        print(f"Values {values} added into table {self.table_name}")

    def delete(self, id_: int):
        self.engine.execute(
            f"DELETE FROM {self.table_name} WHERE id = {id_}"
        )
        print(f"ROW with id={id_} deleted from table {self.table_name}")


if __name__ == "__main__":
    e = Engine("lib.db", auto_connect=True)
    c = CRUD(e)
    t = Table(e, "Books", ("name", "author"))
    # print(t.select(fields=("id", "name", "author")))
    # t.update("author", "A.S. Pushkin", "Pushkin")
    print(t.select(fields=("id", "name", "author")))
    # t.insert(("Harry Potter 3", "J.K. Rowling"))
    t.delete(3)

    # f = [
    #     ("id", "integer primary key autoincrement"),
    #     ("firstname", "varchar"),
    #     ("lastname", "varchar"),
    #     ("year_of_birth", "integer"),
    # ]
    #
    # c.create_table("authors", f)
    # # c.drop_table("authors")
    # c.alter_table("authors", "add", "country", "varchar(30)")
    # c.alter_table("authors", "drop", "country")

    c.engine.disconnect_from_db()



