import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 36.834430  # Your latitude
MY_LONG = 32.485310  # Your longitude
MY_EMAIL = "konjaria1010@gmail.com"
MY_PASSWORD = "oxpljasaggmjdpke"
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

iss_position = {
    "latitude": iss_latitude,
    "longitude": iss_longitude
}
# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_time = time_now.hour


def send_email(From, To, smtp, message_body, Subject=""):
    with smtplib.SMTP(smtp) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=From,
                            to_addrs=To,
                            msg=f"Subject: {Subject}\n\n {message_body}")


def isItDarkNow(hour):
    return hour >= 19


def issPositionIsCloseToMine(iss_long, iss_lat, my_lng, my_lat):
    DifferenceBetweenLongitudes = abs(iss_long - my_lng)
    DifferenceBetweenLatitudes = abs(iss_lat - my_lat)
    return DifferenceBetweenLongitudes <= 5 or DifferenceBetweenLatitudes <= 5


while True:
    time.sleep(60)
    if issPositionIsCloseToMine(
            iss_long=iss_position["longitude"],
            iss_lat=iss_position["latitude"],
            my_lat=MY_LAT,
            my_lng=MY_LONG) and isItDarkNow(current_time):
        body_text = f"ISS is near with you\n\t\tSunrise Time: {sunrise}\n\t\tSunset Time: {sunset}\n\t\tKind Regards,\n\n Sent via " \
                    f"Python Programming Language from the Future "

        send_email(From=MY_EMAIL, To=MY_EMAIL, smtp="smtp.gmail.com", message_body=body_text, Subject="Look Up ☝")
        break