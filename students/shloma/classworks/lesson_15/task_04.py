# Транзакция

from sqlalchemy import create_engine


engine = create_engine("sqlite:///test.db")     # подключение к БД

conn = engine.connect()     # запрос к БД

trans = conn.begin()

conn.execute("""insert into user (firstname, lastname) values (:firstname, :lastname)""",
             firstname="Pasha", lastname='Ivanov')

trans.commit()      # Применение транзакции (.rollback - отмена транзакции)
conn.close()