import os
import json
from getpass import getpass
from utils.validations import (
    validate_email,
    validate_not_empty_str,
    validate_password_match,
    validate_egyptian_phone,
)
from utils.json_utils import add_to_json, read_json
from utils.output_utils import print_green, print_red


def register():
    print()

    while True:
        first_name = input("First Name: ").strip()
        if validate_not_empty_str(first_name):
            break

    while True:
        last_name = input("Last Name: ").strip()
        if validate_not_empty_str(last_name):
            break

    while True:
        email = input("Email: ").strip()
        if validate_email(email):
            break

    while True:
        password = getpass().strip()
        if validate_not_empty_str(password):
            break

    while True:
        confirm_password = getpass("Confirm Password: ").strip()
        if validate_password_match(password, confirm_password):
            break

    while True:
        phone = input("Phone: ").strip()
        if validate_egyptian_phone(phone):
            print_red("Error: Phone isn't a valid egyptian number")
            break

    # TODO: HASH PASSWORD

    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone,
    }

    add_to_json(user, "users.json")

    print_green("Registeration done successfully\n")


def login():
    print()
    email = input("Email: ").strip()
    password = getpass().strip()

    users_data = read_json("users.json")

    if users_data is not None:
        user = next((user for user in users_data if user["email"] == email), None)

        if user is not None and user["password"] == password:
            return user

    print_red("Error: Incorrect email or password\n")
    return False
