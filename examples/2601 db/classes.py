class Table:
    import sqlalchemy
    SELECT = "select {fields} from {table}"

    def __init__(self, db_name, t_name, fields):
        self.db_name = db_name
        self.table_name = t_name
        self.fields = fields
        self.create_engine()

    def create_engine(self):
        self.engine = self.sqlalchemy.create_engine("sqlite:///{}".format(self.db_name))

    def select(self, fields=()):
        return list(self.engine.execute(
            self.SELECT.format(
                fields={', '.join(map(str, fields))} if fields else "*",
                table=self.table_name
            )
        ))
