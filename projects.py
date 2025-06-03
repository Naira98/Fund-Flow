from utils.validations import (
    validate_empty_str,
    validate_money,
    validate_date,
    convert_to_date,
    validate_end_date_after_start_date,
)
from utils.json_utils import add_to_json, delete_from_json, read_json
from utils.output_utils import print_green, print_red


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

    # Get new project index from file
    projects_data = read_json("projects.json")
    if projects_data and isinstance(projects_data, list):
        max_id = max((project.get("id", 0) for project in projects_data), default=0)
        id = max_id + 1
    else:
        id = 1

    project = {
        "id": id,
        "owner": email,
        "title": title,
        "details": details,
        "amount": amount,
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
    }

    add_to_json(project, "projects.json")

    print_green("Project created successfully\n")


def view_projects(email):
    projects_data = read_json("projects.json")

    if projects_data is not None:
        user_projects = [
            project for project in projects_data if project["owner"] == email
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


def delete_project(email):
    projects_data = read_json("projects.json")
    if projects_data is None:
        print_red("No projects data found.\n")
        return

    user_projects = list(
        filter(
            lambda project: isinstance(project, dict) and project.get("owner") == email,
            projects_data,
        )
    )

    if not user_projects:
        print_red("No projects data is found owned by you.\n")
        return

    print("Your Projects")
    for idx, project in enumerate(user_projects, 1):
        print(f"{idx}) {project['title']}")

    try:
        project_no = int(input("Enter project number to delete: "))
        if project_no < 1 or project_no > len(user_projects):
            raise ValueError()
        project_to_delete = user_projects[project_no - 1]
        delete_from_json(
            lambda project: project["id"] == project_to_delete["id"],
            "projects.json",
        )
        print_green(f"Project \'{project_to_delete['title']}\' deleted successfully.\n")
    except Exception:
        print_red("Error: Invalid project number\n")
