# Получение данных

from sqlalchemy import create_engine

e = create_engine("sqlite:///test.db")

result = e.execute("""select * from user""")

for user in result:
    print(user)