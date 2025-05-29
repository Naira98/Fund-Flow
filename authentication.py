from getpass import getpass
from utils import validate_email, validate_empty_str, validate_password_match, validate_egyptian_phone, write_json

def register():
    is_valid_user = True
    print()
    
    first_name = input("First Name: ").strip()
    is_valid_user = validate_empty_str(first_name)
    if not is_valid_user:
        return False

    last_name = input("Last Name: ").strip()
    is_valid_user = validate_empty_str(last_name)
    if not is_valid_user:
        return False
    
    email = input("Email: ").strip()
    is_valid_user = validate_email(email)
    if not is_valid_user:
        return False
    
    password = getpass().strip()
    is_valid_user = validate_empty_str(password)
    if not is_valid_user:
        return False
    
    confirm_password = getpass("Confirm Password: ").strip()
    is_valid_user = validate_password_match(password, confirm_password)
    if not is_valid_user:
        return False

    phone = input("Phone: ").strip()
    is_valid_user = validate_egyptian_phone(phone)
    if not is_valid_user:
        print("Error: Phone isn't a valid egyptian number\n")
        return False

# TODO: HASH PASSWORD

    user = {
       "first_name": first_name,
       "last_name": last_name,
       "email": email,
       "password": password,
       "phone": phone
    }

    write_json(user, 'users.json')
