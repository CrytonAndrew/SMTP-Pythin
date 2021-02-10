import pandas
import datetime as dt
import smtplib
import random

MY_EMAIL = ""
MY_PASSWORD = ""

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt", "letter_4.txt",  "letter_5.txt"]


contacts = pandas.read_csv("contacts.csv")
contact_dict = contacts.to_dict(orient="records")
for person in contact_dict:
    now = dt.datetime.now()
    if person["month"] == now.month and person["day"] == now.day:
        name = person["name"]
        email = person["email"]
        open_string = f"Hi {name}"
        closing_string = f"Lots of Love Cryton"
        with open(random.choice(letters)) as letter:
            content = letter.readlines()
            letter_string = ''
            for line in content:
                letter_string += line

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject: Happy Birthday\n\n {open_string} \n {letter_string} \n {closing_string}")


