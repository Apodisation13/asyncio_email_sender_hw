import asyncio
import aiosqlite
from datetime import datetime

from email_try import send_message


async def send_email_to_all_from_db():
    """подключаемся к db, берем список почт, асинхронно отсылаем письма туда"""
    db = await aiosqlite.connect('contacts.db')
    cursor = await db.execute('SELECT email FROM contacts')
    rows = await cursor.fetchall()  # как надо сделать
    # rows = ["apodisation13@gmail.com"] * 10  # тест отправить себе 10 раз
    tasks = []
    for mail in rows:
        task = asyncio.create_task(send_message(mail[0]))  # mail[0] - там кортежи (elem,)
        tasks.append(task)
    await asyncio.gather(*tasks)
    await cursor.close()
    await db.close()


if __name__ == '__main__':
    t1 = datetime.now()
    asyncio.run(send_email_to_all_from_db())
    t2 = datetime.now()
    print(t2 - t1)
