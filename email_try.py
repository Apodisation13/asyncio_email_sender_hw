from datetime import datetime
from email.message import EmailMessage
from aiosmtplib import SMTP
import smtplib


with open('password.txt') as f:
    PASSWORD = f.readline()
SENDER = "apodisation13@gmail.com"


async def send_message(receiver: str):
    """отправить письмо receiver то sender"""
    message = EmailMessage()
    message["From"] = SENDER
    message["To"] = receiver
    message["Subject"] = "Hello World!"

    smtp_client = SMTP('smtp.gmail.com',587)  # это из aiosmtplib
    await smtp_client.connect()
    await smtp_client.ehlo()
    await smtp_client.starttls()
    await smtp_client.ehlo()
    await smtp_client.login(SENDER, PASSWORD)

    message.set_content(f"Привет {receiver}")
    await smtp_client.sendmail(SENDER, receiver, message.as_string())
    print(f'отправлено 1 сообщение для {receiver}')


def without_async():
    """та же функция, но без асинк"""
    recipients = ["apodisation13@gmail.com"] * 5  # отправляю себе 10 писем

    message = EmailMessage()
    message["From"] = SENDER
    message["To"] = ', '.join(recipients)
    message["Subject"] = "Hello World!"

    smtp_client = smtplib.SMTP('smtp.gmail.com')  # а здесь smtplib
    smtp_client.ehlo()
    smtp_client.starttls()
    smtp_client.ehlo()
    smtp_client.login(SENDER, PASSWORD)

    for mail in recipients:  # в recipients можно положить любой список почт
        message.set_content(f"Привет {mail}")
        smtp_client.sendmail(SENDER, mail, message.as_string())
        print(f'отправлено 1 сообщение для {mail}')


if __name__ == '__main__':
    t1 = datetime.now()
    without_async()
    t2 = datetime.now()
    print(t2 - t1)
