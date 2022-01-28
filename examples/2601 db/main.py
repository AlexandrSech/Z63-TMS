from classes import Table


books = Table("lib.db", "books", ("id", "name", "author"))
sel_res = books.select()
print(sel_res)









"""import sqlalchemy


engine = sqlalchemy.create_engine("sqlite:///lib.db")

select = engine.execute(
    "select * from books"
)
for line in select:
    print(line)


conn = engine.connect()
trans = conn.begin()
conn.execute(
"insert into user (firstname, lastname) values (:firstname, :lastname)",
firstname="Pasha", lastname='Ivanov')
trans.commit()
conn.close()
"""
