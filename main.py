import smtplib
import datetime as dt
import random

MY_EMAIL = "kibetnim@gmail.com"
PASSWORD = "replacewithyourgoogleapp-password"


# Read Quotes from file
def read_quotes():
    with open("quotes.txt", "r") as file:
        quotes_list = file.readlines()
        random_quote = random.choice(quotes_list)
    return random_quote


# Activating email send
def motivation():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Secure connection
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="nmandelakibe@gmail.com",
                            msg=f"Subject: Motivation\n\n {read_quotes()}"
                            )


# Check if today is monday
today = dt.datetime.now()

current_day_of_week = today.weekday()

if current_day_of_week == 0:
    motivation()
