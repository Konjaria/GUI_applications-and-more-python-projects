import pandas
import datetime as dt
from random import choice
import smtplib

FROM_EMAIL = "konjaria1010@gmail.com"
PASSWORD = "fwhcmmoevmnwxkzz"


def send_email(TO, name, year, message_body):
    year_modified = ""
    if str(year).isdigit():
        year_modified = str(current_year - year)
        if year_modified[len(year_modified) - 1] == "1":
            year_modified += "st"
        elif year_modified[len(year_modified) - 1] == "2":
            year_modified += "nd"
        elif year_modified[len(year_modified) - 1] == "3":
            year_modified += "rd"
        else:
            year_modified += "th"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL,
                            to_addrs=TO,
                            msg=f"Subject:Happy {year_modified} Birthday {name.title()} \n\n {message_body}")


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

date_file = pandas.read_csv("birthdays.csv")
data = date_file.to_dict(orient="records")

todayIsSomeonesBirthday = False
birthday_persons = []
for dictionary in data:
    if dictionary["month"] == current_month and dictionary["day"] == current_day:
        todayIsSomeonesBirthday = True
    if todayIsSomeonesBirthday:
        birthday_persons.append(dictionary)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
if len(birthday_persons) != 0:
    letterTemplates = [
        "./letter_templates/letter_1.txt",
        "./letter_templates/letter_2.txt",
        "./letter_templates/letter_3.txt"
    ]

    for i in range(len(birthday_persons)):
        random_letter = choice(letterTemplates)
        with open(random_letter, "r") as dataFile:
            textContent = dataFile.readlines()
        message_body = ""
        numberOfOccurences = 0
        for string in textContent:
            if "[NAME]" in string:
                numberOfOccurences += 1
                if numberOfOccurences == 1:
                    string = string.replace("[NAME]", birthday_persons[i]["name"])
                else:
                    string = string.replace("[NAME]", "")
                message_body += string
            else:
                message_body += string
        send_email(birthday_persons[i]["email"],
                   birthday_persons[i]["name"],
                   birthday_persons[i]["year"],
                   message_body)

# 4. Send the letter generated in step 3 to that person's email address.
