
import smtplib, random
import datetime as dt


my_email = "adegbitefeyisetan@gmail.com"
my_password = "fovk opsk spir tdil" # App password generated from google account

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("./day32-email-datetime/quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        # connection.starttls() # make connect secure
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=my_email,
                            msg=f"Subject:Morning Motivation\n\n{quote}")
