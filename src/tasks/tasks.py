import smtplib
from email.message import EmailMessage

from celery import Celery
from src.config import SMTP_USER, SMTP_PASSWORD, REDIS_HOST, REDIS_PORT

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')


def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = "Информация об отчёте"
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;"> Здравствуйте, {username}, а вот и ваш отчет!</h1>'
        '/div',
        subtype='html'

    )
    return email

@celery.task # Обернули задачу 
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)