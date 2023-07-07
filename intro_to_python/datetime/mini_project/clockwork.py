from datetime import datetime, timezone
import pytz
import time
import os


def get_time(timezone):
    return utc_dt.astimezone(timezone).strftime("%H:%M:%S")



if __name__=="__main__":
    while True:
        utc_dt = datetime.now()
        paris = pytz.timezone("Europe/Paris")
        douala = pytz.timezone("Africa/Douala")

        print("Heure Douala: {} <---> Heure Paris: {}".format(get_time(douala), get_time(paris)))
        time.sleep(1)
        os.system("cls")
    