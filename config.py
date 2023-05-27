from os import path
from dotenv import dotenv_values


CONFIG = {
    **dotenv_values(path.join(path.dirname(__file__), ".env")),
    **dotenv_values(path.join(path.dirname(__file__), ".env.local")),
}

URL = CONFIG["URL"]
FILE = CONFIG["FILE"]
LAKE = CONFIG["LAKE"]
TRESHOLD = int(CONFIG["TRESHOLD"])
SMTP_SERVER = CONFIG["SMTP_SERVER"]
SMTP_LOGIN = CONFIG["SMTP_LOGIN"]
SMTP_PASSWORD = CONFIG["SMTP_PASSWORD"]
MAIL_FROM = CONFIG["MAIL_FROM"]
MAIL_TO = CONFIG["MAIL_TO"]
MAIL_SUBJECT = CONFIG["MAIL_SUBJECT"]
MAIL_BODY = CONFIG["MAIL_BODY"]
