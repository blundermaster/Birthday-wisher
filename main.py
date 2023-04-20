##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# from smtplib import *
# my_email= "20193021.it@gmail.com"
# password="abcd1234"
# connection=SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email, to_addrs="20193021.it@gmail.com", msg="Hello")
# connection.close()

# import datetime as dt
# from smtplib import *
# import random
# l=open("quotes.txt").readlines()
# now=dt.datetime.now()
# day_of_the_week= now.weekday()
# weekday=["Monday","Tuesday", "Wednesday","Thursday","Friday","Saturday", "Sunday"]
# randquote=random.choice(l)
# my_email= "20193021.it@gmail.com"
# password="abcd1234()"
# with SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="20193021.it@gmail.com",
#                         msg=f"Subject:Motivational quote for the day \n\nToday is {weekday[day_of_the_week]} and the quote of the day is {randquote}")



import datetime as dt
import random
from csv import writer
from smtplib import SMTP

from pandas import *
add_birthday=input("do you want to add birthday? Enter y for yes and n for no")
while add_birthday=='y':
    name=input("Enter the name: ")
    email=input("Enter his/her email address: ")
    year= input("Enter the year: ")
    month = input("Enter the month: ")
    day = input("Enter the day: ")
    birth_details=[name,email,year,month,day]
    with open("birthdays.csv",'a',newline="") as f:
        w= writer(f)
        w.writerow(birth_details)

    add_birthday = input("do you want to add birthday? Enter y for yes and n for no")

birthday_dataframe=read_csv("birthdays.csv")

monthtolist=birthday_dataframe["month"].tolist()
daytolist=birthday_dataframe["day"].tolist()
emailtolist=birthday_dataframe["email"].tolist()
nametolist=birthday_dataframe["name"].tolist()
print(monthtolist)
now=dt.datetime.now()

if now.month in monthtolist:
    for i in monthtolist:
        if i==now.month:
            index=monthtolist.index(i)
            if daytolist[i]==now.day:
                my_email= "20193021.it@gmail.com"
                password="abcd1234()"
                letter = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt",
                          "letter_templates/letter_3.txt"]
                randletter = random.choice(letter)
                with open(randletter, mode="r+") as f:
                    data = f.read()
                    data = data.replace("[NAME]", nametolist[index])

                with SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email,password=password)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs=emailtolist[index],
                                        msg=f"Subject: Happy Birthday \n\n {data}")





