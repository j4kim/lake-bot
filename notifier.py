from config import TRESHOLD, SMTP_SERVER, SMTP_LOGIN, SMTP_PASSWORD, MAIL_FROM, MAIL_TO
from smtplib import SMTP
from email.message import EmailMessage

def send(new_temperature):
    print("Connect to SMTP server")
    s = SMTP(SMTP_SERVER)
    s.starttls()
    s.login(SMTP_LOGIN, SMTP_PASSWORD)
    print("Send mail")
    msg = EmailMessage()
    msg['Subject'] = "Lake is hot"
    msg['From'] = MAIL_FROM
    msg['To'] = MAIL_TO
    msg.set_content(f"L'eau du lac est à {new_temperature}° aujourd'hui")
    s.send_message(msg)
    print("Email sent")


def check_and_notify(new_temperature, old_temperature):
    if old_temperature == new_temperature:
        print("Temperature did not change")
        return

    print(f"Temperature changed from {old_temperature}° to {new_temperature}°")

    if new_temperature > old_temperature and new_temperature >= TRESHOLD:
        print("Temperature increased and is above treshold, sending notification")
        send(new_temperature)
