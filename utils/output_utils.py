from utils.json_utils import read_json


RED = "\033[31m"
GREEN = "\033[32m"
END = "\033[0m"


def print_red(message):
    print(f"{RED}{message}{END}")


def print_green(message):
    print(f"{GREEN}{message}{END}")


def show_projects(projects):
    if not projects:
        print_red("Error: No projects found.")
        return

    print("\nYour Projects:")
    print("═" * 40)
    for idx, project in enumerate(projects, 1):
        print(f"Project #{idx}")
        print("─" * 40)
        print(f"Title        : {project['title']}")
        print(f"Details      : {project['details']}")
        print(f"Target Amount: {project['amount']} EGP")
        print(f"Start Date   : {project['start_date']}")
        print(f"End Date     : {project['end_date']}")
        print("═" * 40)


def choose_from_your_projects(email, purpose):
    projects_data = read_json("projects.json")
    if projects_data is None:
        print_red("Error: No projects found for you.")
        return

    user_projects = [
        project for project in projects_data
        if isinstance(project, dict) and project.get("owner") == email
    ]

    if not user_projects:
        print_red("Error: No projects found owned by you.")
        return

    print()
    print("╔══════════════════════════╗")
    print("║      Your Projects       ║")
    print("╚══════════════════════════╝")

    for idx, project in enumerate(user_projects, 1):
        print(f"{idx}) {project['title']}")

    try:
        project_no = int(input(f"Project number to {purpose}: "))
        if project_no < 1 or project_no > len(user_projects):
            raise ValueError()
        return user_projects[project_no - 1]

    except Exception:
        print_red("Error: Invalid project number.\n")
