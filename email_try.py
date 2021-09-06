import datetime
from email.message import EmailMessage

from aiosmtplib import SMTP
import smtplib


with open('password.txt') as f:
    password = f.readline()
sender = "apodisation13@gmail.com"


async def send_message(receiver: str):

    message = EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = "Hello World!"

    smtp_client = SMTP('smtp.gmail.com',587)
    await smtp_client.connect()
    await smtp_client.ehlo()
    await smtp_client.starttls()
    await smtp_client.ehlo()
    await smtp_client.login(sender, password)

    message.set_content(f"Привет {receiver}")
    await smtp_client.sendmail(sender, receiver, message.as_string())
    print(f'отправлено 1 сообщение для {receiver}')


def without_acync():
    recipients = ["apodisation13@gmail.com"] * 10

    message = EmailMessage()
    message["From"] = sender
    message["To"] = ', '.join(recipients)
    message["Subject"] = "Hello World!"

    smtp_client = smtplib.SMTP('smtp.gmail.com')
    smtp_client.ehlo()
    smtp_client.starttls()
    smtp_client.ehlo()
    smtp_client.login(sender, password)

    for each in recipients:
        message.set_content(f"Привет {each}")
        smtp_client.sendmail(sender, each, message.as_string())
        print(f'отправлено 1 сообщение для {each}')


if __name__ == '__main__':
    t1 = datetime.datetime.now()
    without_acync()
    t2 = datetime.datetime.now()
    print(t2 - t1)
