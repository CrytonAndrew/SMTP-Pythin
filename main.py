import smtplib

my_email = "@gmail.com"
my_password = ""
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="@gmail.com",
        msg="Subject:This is the subject \n\n This the body")

