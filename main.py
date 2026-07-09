##################### Extra Hard Starting Project ######################
import smtplib,datetime as dt, pandas as pd
from random import randint
import os
# 1. Update the birthdays.csv
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
birthdays = pd.read_csv("birthdays.csv")
birthday_tuple = (now.day, now.month)
birthdays_dict = {(data_row.day,data_row.month):data_row for (index,data_row) in birthdays.iterrows()}
if birthday_tuple in birthdays_dict:
    birthday_person = birthdays_dict[birthday_tuple]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(f"letter_templates/letter_{randint(1,3)}.txt") as file:
        message = file.read().replace("[NAME]",birthday_person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587, timeout=10) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject: Happy birthday {birthday_person['name']}!\n\n{message}"
            )



