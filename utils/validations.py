import re
import json
import os

def validate_empty_str(str):
    if len(str) == 0:
        print("Error: Value can't be empty\n")
        return False
    
    return True

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid =  bool(re.match(email_regex, email))

    if is_valid and os.path.exists('users.json'):
        with open('users.json', 'r') as file:
            users_data = json.load(file)
            res = next((user for user in users_data if user['email'] == email), None)

            if res is not None:
                print("Error: Email already exists\n")
                return False

    return True


def validate_password_match(password, confirm_password):
    if password != confirm_password:
        print("Error: Passwords don't match\n")
        return False

    return True

def validate_egyptian_phone(phone):
    phone_regex = r'^01[0-2,5]\d{8}$'
    is_valid = bool(re.match(phone_regex, phone))
    if not is_valid:
        print("Error: Phone isn't a valid egyptian number\n")
        return False
    
    return True

