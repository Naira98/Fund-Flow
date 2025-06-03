from utils.validations import (
    validate_empty_str,
    validate_money,
    validate_date,
    convert_to_date,
    validate_end_date_after_start_date,
)
from utils.json_utils import add_to_json, delete_from_json, read_json
from utils.output_utils import (
    print_green,
    print_red,
    show_projects,
    choose_from_your_projects,
)


def create_project(email):
    title = input("\nTitle: ").strip()
    if not validate_empty_str(title):
        return False

    details = input("Details: ").strip()
    if not validate_empty_str(details):
        return False

    amount = input("Traget amount (EGP): ").strip()
    if not validate_money(amount):
        return False

    start_date = input("Start date (YYYY-MM-DD): ").strip()
    if not validate_date(start_date):
        return False
    start_date = convert_to_date(start_date)

    end_date = input("End date (YYYY-MM-DD): ").strip()
    if not validate_date(end_date):
        return False

    end_date = convert_to_date(end_date)
    if not validate_end_date_after_start_date(start_date, end_date):
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


def view_projects():
    projects_data = read_json("projects.json")
    show_projects(projects_data)


def delete_project(email):
    choosen_project = choose_from_your_projects(email, "delete")
    if choosen_project is None:
        return

    delete_from_json(
        lambda project: project["id"] == choosen_project["id"],
        "projects.json",
    )
    print_green(f"Project '{choosen_project['title']}' deleted successfully.\n")


def search_by_date():
    date = input("\nDate (YYYY-MM-DD): ").strip()

    if not validate_date(date):
        return False

    projects_data = read_json("projects.json")
    if projects_data is None:
        print_red("No projects data found.\n")
        return

    projects = list(
        filter(
            lambda project: isinstance(project, dict)
            and (project.get("start_date") == date or project.get("end_date") == date),
            projects_data,
        )
    )

    show_projects(projects)


def edit_project(email):
    choosen_project = choose_from_your_projects(email, "edit")
    if choosen_project is None:
        return
    pass
