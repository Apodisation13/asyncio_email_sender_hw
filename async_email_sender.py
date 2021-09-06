import asyncio
import datetime

import aiosqlite
from sqlalchemy.orm import sessionmaker
from models import *
from email_try import send_message


path = 'sqlite:////home/james/PycharmProjects/asyncio_hw/contacts.db'
engine = sq.create_engine(path)

Session = sessionmaker(bind=engine)
session = Session()

# q = engine.execute('SELECT * FROM contacts').first()
# print(q)
#
# q = session.query(Contact.contact_id, Contact.email).order_by(Contact.contact_id).limit(1)
# print(q)
# print(q[0].email)


async def sql():
    db = await aiosqlite.connect('contacts.db')
    cursor = await db.execute('SELECT email FROM contacts')
    rows = await cursor.fetchmany(5)
    rows = ["apodisation13@gmail.com"] * 10
    tasks = []
    for each in rows:
        task = asyncio.create_task(send_message(each))
        tasks.append(task)
    await asyncio.gather(*tasks)
    # await cursor.close()
    # await db.close()


if __name__ == '__main__':
    t1 = datetime.datetime.now()
    asyncio.run(sql())
    t2 = datetime.datetime.now()
    print(t2 - t1)
