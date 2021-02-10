import smtplib
import datetime as dt
import random

with open("quotes.txt") as file:
    quotes = file.readlines()

now = dt.datetime.now()

if now.weekday() == 0:
    my_email = ""
    my_password = ""
    quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=f"Subject: Monday Motivation \n\n {quote}")


