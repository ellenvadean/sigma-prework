"""age"""
# L3 Challenge 3 Task 1
# Age Calculator

import datetime


def input_DOB():
    date_input = input("Please input DOB in dd-mm-yyyy format: ")
    day = int(date_input[:2])
    month = int(date_input[3:5])
    year = int(date_input[-4:])
    dob = datetime.datetime(year, month, day)
    return dob


date_of_birth = input_DOB()
date_today = datetime.datetime.now()


def get_age(dob):
    years = date_today.year-dob.year
    if date_today.month < dob.month:
        years -= 1
    elif date_today.month == dob.month:
        if date_today.day < dob.day:
            years -= 1
    return years


age = (get_age(date_of_birth))
print(f"You are {age} years old.")
