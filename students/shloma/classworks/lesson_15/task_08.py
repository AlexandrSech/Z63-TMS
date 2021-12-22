# Создание запроса Query

from task_07 import *

person = session.query(Person).filter_by(firstname="Alex").first()
print(person)

person = session.query(Person).filter(Person.firstname=="Alex").first()
print(person)

person = session.query(Person).filter(((Person.firstname=="Alex") & (Person.lastname=="Varkalov"))).all()
print(person)