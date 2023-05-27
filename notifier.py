from config import TRESHOLD


def check_and_notify(new_temperature, old_temperature):
    if new_temperature > old_temperature and new_temperature > TRESHOLD:
        print("Temperature increased and is above treshold, sending notification")
