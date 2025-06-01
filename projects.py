from utils.validations import (
    validate_empty_str,
    validate_money,
    validate_date,
    convert_to_date,
    validate_end_date_after_start_date,
)
from utils.json_utils import write_json, read_json
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


def view_projects(email):
    projects_date = read_json("projects.json")

    if projects_date is not None:
        user_projects = [
            project for project in projects_date if project["owner"] == email
        ]

        if not user_projects:
            print("No projects found for this user.\n")
            return
        
        print("\nYour Projects:")
        print("=" * 40)
        for idx, project in enumerate(user_projects, 1):
            print(f"Project #{idx}")
            print("-" * 40)
            print(f"Title        : {project['title']}")
            print(f"Details      : {project['details']}")
            print(f"Target Amount: {project['amount']} EGP")
            print(f"Start Date   : {project['start_date']}")
            print(f"End Date     : {project['end_date']}")
            print("=" * 40)

        # TODO:PRINT DATA IN DYNAMIC TABLE
