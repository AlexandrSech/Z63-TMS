# Добавление записей

from sqlalchemy import create_engine


e = create_engine("sqlite:///test.db")
e.execute("""
    insert into user (firstname, lastname)
    values ('Alex', 'Varkalov')
    """)


e.execute("""
    insert into user (firstname, lastname)
    values ('Sergey', 'Shloma')
    """)