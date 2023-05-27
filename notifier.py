import config
from smtplib import SMTP
from email.message import EmailMessage

def send(new_temperature):
    print("Connect to SMTP server")
    s = SMTP(config.SMTP_SERVER)
    s.starttls()
    s.login(config.SMTP_LOGIN, config.SMTP_PASSWORD)
    print("Send email")
    msg = EmailMessage()
    msg['Subject'] = config.MAIL_SUBJECT
    msg['From'] = config.MAIL_FROM
    msg['To'] = config.MAIL_TO
    msg.set_content(config.MAIL_BODY.format(new_temperature))
    s.send_message(msg)
    print("Email sent")


def check_and_notify(new_temperature, old_temperature):
    if old_temperature == new_temperature:
        print("Temperature did not change")
        return

    print(f"Temperature changed from {old_temperature}° to {new_temperature}°")

    if new_temperature > old_temperature and new_temperature >= config.TRESHOLD:
        print("Temperature increased and is above treshold, sending notification")
        send(new_temperature)
