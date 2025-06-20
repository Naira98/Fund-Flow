from utils.validations import (
    validate_not_empty_str,
    validate_money,
    validate_date,
    convert_to_date,
    validate_end_date_after_start_date,
)
from utils.json_utils import add_to_json, delete_from_json, read_json, update_json_by_id
from utils.output_utils import (
    print_green,
    print_red,
    show_projects,
    choose_from_your_projects,
)
from typing import Optional


def create_project(email):
    print()
    while True:
        title = input("Title: ").strip()
        if validate_not_empty_str(title):
            break

    while True:
        details = input("Details: ").strip()
        if validate_not_empty_str(details):
            break

    while True:
        amount = input("Traget amount (EGP): ").strip()
        if validate_money(amount):
            break

    while True:
        start_date = input("Start date (YYYY-MM-DD): ").strip()
        if not validate_date(start_date):
            continue
        start_date = convert_to_date(start_date)
        break

    while True:
        end_date = input("End date (YYYY-MM-DD): ").strip()
        if not validate_date(end_date):
            continue

        end_date = convert_to_date(end_date)
        if validate_end_date_after_start_date(start_date, end_date):
            break

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

    print_green("Project created successfully")


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
    print_green(f"Project '{choosen_project['title']}' deleted successfully.")


def search_by_date():
    print()
    date = input("Date (YYYY-MM-DD): ").strip()

    if not validate_date(date):
        return False

    projects_data = read_json("projects.json")
    if projects_data is None:
        print_red("Error: No projects found have this date.")
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

    updated_values: dict[str, Optional[str]] = {
        "title": None,
        "details": None,
        "amount": None,
        "start_date": None,
        "end_date": None,
    }

    while True:
        choice_number = 1

        print()
        print("╔══════════════════════════╗")
        print("║      Project Fileds      ║")
        print("╚══════════════════════════╝")

        for key, value in updated_values.items():
            print(f'{choice_number}) [{"*" if value else " "}] {key}')
            choice_number += 1
        print(f"{choice_number}) # Done")

        try:
            filed_number = int(input("Field number to update: "))
            if (filed_number > len(updated_values) + 1) or filed_number <= 0:
                raise Exception()
        except:
            print_red("Error: Invalid filed number.")
            break

        if 1 <= filed_number <= 5:
            key = list(updated_values.keys())[filed_number - 1]
            if updated_values[key] is not None:
                if key == "start_date":
                    start_date = convert_to_date(choosen_project["start_date"])
                    end_date = convert_to_date(
                        updated_values["end_date"] or choosen_project["end_date"]
                    )

                    if not validate_end_date_after_start_date(
                        start_date,
                        end_date,
                        "Error: Cannot remove the updated start date because the end date must be after the original start date.",
                    ):
                        continue

                elif key == "end_date":
                    start_date = convert_to_date(
                        updated_values["start_date"] or choosen_project["start_date"]
                    )
                    end_date = convert_to_date(choosen_project["end_date"])

                    if not validate_end_date_after_start_date(
                        start_date,
                        end_date,
                        "Error: Cannot remove the updated end date because the original end date must be after the start date.",
                    ):
                        continue

                updated_values[key] = None
                continue

        if filed_number == 1:  # title
            title = input("Title: ").strip()
            if validate_not_empty_str(title):
                updated_values["title"] = title

        elif filed_number == 2:  # details
            details = input("Details: ").strip()
            if validate_not_empty_str(details):
                updated_values["details"] = details

        elif filed_number == 3:  # amount
            amount = input("Traget amount (EGP): ").strip()
            if validate_money(amount):
                updated_values["amount"] = amount

        elif filed_number == 4:  # start_date
            start_date = input("Start date (YYYY-MM-DD): ").strip()

            if validate_date(start_date):
                start_date = convert_to_date(start_date)
                end_date = convert_to_date(
                    updated_values["end_date"] or choosen_project["end_date"]
                )

                if validate_end_date_after_start_date(start_date, end_date):
                    updated_values["start_date"] = start_date.strftime("%Y-%m-%d")

        elif filed_number == 5:  # end_date
            end_date = input("End date (YYYY-MM-DD): ").strip()

            if validate_date(end_date):
                start_date = convert_to_date(
                    updated_values["start_date"] or choosen_project["start_date"]
                )
                end_date = convert_to_date(end_date)

                if validate_end_date_after_start_date(start_date, end_date):
                    updated_values["end_date"] = end_date.strftime("%Y-%m-%d")

        elif filed_number == 6:  # done
            update_json_by_id(
                {
                    **choosen_project,
                    **{
                        key: value
                        for key, value in updated_values.items()
                        if value is not None
                    },
                },
                "projects.json",
            )
            print_green("Project updated successfully")
            break

        continue
