import re
import json
import os
import datetime
from utils.output_utils import print_red


def validate_empty_str(str):
    if len(str) == 0:
        print_red("Error: Value can't be empty\n")
        return False

    return True


def validate_email(email):
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    is_valid = bool(re.match(email_regex, email))

    if is_valid and os.path.exists("users.json"):
        with open("users.json", "r") as file:
            users_data = json.load(file)
            res = next((user for user in users_data if user["email"] == email), None)

            if res is not None:
                print_red("Error: Email already exists\n")
                return False

    return True


def validate_password_match(password, confirm_password):
    if password != confirm_password:
        print_red("Error: Passwords don't match\n")
        return False

    return True


def validate_egyptian_phone(phone):
    phone_regex = r"^01[0-2,5]\d{8}$"
    is_valid = bool(re.match(phone_regex, phone))
    if not is_valid:
        print_red("Error: Phone isn't a valid egyptian number\n")
        return False

    return True


def validate_money(amount):
    try:
        target = float(amount)
        if target <= 0:
            print_red("Error: Traget amount must be a positive number\n")
            return False
        return True

    except ValueError:
        print_red("Error: Traget amount must be a number\n")
        return False


def validate_date(date):
    # From 2000-01-01 To 2029-12-31
    date_regex = r"^20[0-2][0-9]-((0[1-9])|(1[0-2]))-(0[1-9]|[1-2][0-9]|3[0-1])$"
    is_valid = bool(re.match(date_regex, date))
    if not is_valid:
        print_red("Error: Date must be in a range from 2000 to 2029\n")
        return False

    return True


def convert_to_date(date):
    [year, month, day] = date.split("-")
    date = datetime.datetime(int(year), int(month), int(day))
    return date


def validate_end_date_after_start_date(start_date, end_date):
    if end_date <= start_date:
        print_red("Error: End date must be after start date\n")
        return False

    return True
