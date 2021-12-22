# Session

from task_06 import *
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()
session.add(Person('Alex', 'Varkalov'))
session.add_all([Person('Alex', 'Petrov'), Person('Ann', 'Ivanova')])
session.add(Person('Sergey', 'Shloma'))
session.commit()