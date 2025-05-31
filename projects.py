from utils.validations import (
    validate_empty_str,
    validate_money,
    validate_date,
    convert_to_date,
    validate_end_date_after_start_date,
)
from utils.json_utils import write_json
from utils.output_utils import print_green


def create_project(email):
    is_valid_project = True
    print()

    title = input("Title: ").strip()
    is_valid_project = validate_empty_str(title)
    if not is_valid_project:
        return False

    details = input("Details: ").strip()
    is_valid_project = validate_empty_str(details)
    if not is_valid_project:
        return False

    amount = input("Traget amount (EGP): ").strip()
    is_valid_project = validate_money(amount)
    if not is_valid_project:
        return False

    start_date = input("Start date (YYYY-MM-DD): ").strip()
    is_valid_project = validate_date(start_date)
    if not is_valid_project:
        return False
    start_date = convert_to_date(start_date)

    end_date = input("End date (YYYY-MM-DD): ").strip()
    is_valid_project = validate_date(end_date)
    if not is_valid_project:
        return False

    end_date = convert_to_date(end_date)
    is_valid_project = validate_end_date_after_start_date(start_date, end_date)
    if not is_valid_project:
        return False

    project = {
        "owner": email,
        "title": title,
        "details": details,
        "amount": amount,
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
    }

    write_json(project, "projects.json")

    print_green("Project created successfully\n")
