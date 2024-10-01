
from datetime import datetime
import smtplib, requests, time

MY_LAT = 1.2243
MY_LNG = 52.432
my_email = "adegbitefeyisetan@gmail.com"
my_password = "fovk opsk spir tdil"

def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    # print(data)
    print(data["timestamp"])

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LNG-5 <= iss_lng <= MY_LNG+5:
        return True


def is_night():
    params = {"lat": MY_LAT,"lng": MY_LNG, "formatted": 0}

    res = requests.get("https://api.sunrise-sunset.org/json", params=params)
    res.raise_for_status()
    data = res.json()
    print(data)
    sunrise = int(data['results']['sunrise'].split["T"][1].split(":")[0])
    sunset = int(data['results']['sunset'].split["T"][1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    # Send email 
    if is_iss_overhead() and is_night():
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs=my_email,
                                msg=f"Subject:Look up for ISS\n\nQuickly check the sky the ISS is above you now, Hurry!!!")
            print("Mail Sent successfully.")

    time.sleep(60) # check every sixty seconds

