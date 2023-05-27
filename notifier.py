from config import TRESHOLD


def check_and_notify(new_temperature, old_temperature):
    if old_temperature == new_temperature:
        print("Temperature did not change")
        return

    print(f"Temperature changed from {old_temperature}° to {new_temperature}°")

    if new_temperature > old_temperature and new_temperature >= TRESHOLD:
        print("Temperature increased and is above treshold, sending notification")
