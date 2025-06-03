RED = "\033[31m"
GREEN = "\033[32m"
NC = "\033[0m"

def print_red(message):
    print(f"{RED}{message}{NC}")

def print_green(message):
    print(f"{GREEN}{message}{NC}")

def show_projects(projects):
    if not projects:
        print("No projects found for this user.\n")
        return

    print("\nYour Projects:")
    print("=" * 40)
    for idx, project in enumerate(projects, 1):
        print(f"Project #{idx}")
        print("-" * 40)
        print(f"Title        : {project['title']}")
        print(f"Details      : {project['details']}")
        print(f"Target Amount: {project['amount']} EGP")
        print(f"Start Date   : {project['start_date']}")
        print(f"End Date     : {project['end_date']}")
        print("=" * 40)

    # TODO:PRINT DATA IN DYNAMIC TABLE
