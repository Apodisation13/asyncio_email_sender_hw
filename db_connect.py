from sqlalchemy.orm import sessionmaker
from models import *


path = 'sqlite:////home/james/PycharmProjects/asyncio_hw/contacts.db'
engine = sq.create_engine(path)
Session = sessionmaker(bind=engine)
session = Session()

q = engine.execute('SELECT * FROM contacts').first()
print(q)

q = session.query(Contact.contact_id, Contact.email).order_by(Contact.contact_id).limit(1)
print(q)
print(q[0].email)
