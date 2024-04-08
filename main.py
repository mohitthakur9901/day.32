import datetime as dt
import smtplib
import pandas
import random
my_email=""
my_password=""
time=dt.datetime.now()
today=(time.month,time.day)
data=pandas.read_csv("birthdays.csv")
new_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in new_dict:
    birthday_person=new_dict[today]
    file_path=f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        content=file.read()
        replace=content.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com",25) as connection:
        connection.starttls()
        connection.login(user=my_email,password= my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject: HAPPY BIRTHDAY {replace}")




