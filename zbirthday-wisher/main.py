import smtplib, pandas,random
from datetime import datetime

src_dir = "zbirthday-wisher"
my_email = "adegbitefeyisetan@gmail.com"
my_password = "xxxxxxxxxxxxx" # App password generated from google account


today_tuple = (datetime.now().month, datetime.now().day)

data = pandas.read_csv(f"{src_dir}/birthdays.csv", )

birthdays_dict ={(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"{src_dir}/letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"] )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{content}")
        print("Mail Sent successfully.")
else:
    print("no birthday match found")
