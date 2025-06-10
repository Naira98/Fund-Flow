from authentication import register, login
from projects import create_project, view_projects, delete_project, search_by_date, edit_project
from utils.output_utils import print_red, print_green, clear_terminal

BOLD = "\033[1m"
END = "\033[0m"

while True:
    print("╔════════════════════════════════════╗")
    print("║                                    ║")
    print(f"║      {BOLD}Welcome to Fund Flow!{END}         ║")
    print("║  Your personal finance companion.  ║")
    print("║                                    ║")
    print("║  1) Register                       ║")
    print("║  2) Login                          ║")
    print("║  3) Exit                           ║")
    print("║                                    ║")
    print("╚════════════════════════════════════╝")

    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        user = login()
        if user:
            while True:
                print()
                print("╔════════════════════════════════════╗")
                print(f"║           {BOLD}Projects Menu{END}            ║")
                print("║                                    ║")
                print("║  1) Create Project                 ║")
                print("║  2) View All Projects              ║")
                print("║  3) Edit Project                   ║")
                print("║  4) Delete Project                 ║")
                print("║  5) Search Project by Date         ║")
                print("║  6) Logout                         ║")
                print("╚════════════════════════════════════╝")

                choice = input("Choose an option: ")

                if choice == "1":
                    create_project(user["email"])
                elif choice == "2":
                    view_projects()
                elif choice == "3":
                    edit_project(user["email"])
                elif choice == "4":
                    delete_project(user["email"])
                elif choice == "5":
                    search_by_date()
                elif choice == "6":
                    clear_terminal()
                    # print_green("You have been logged out. See you next time!\n")
                    break
                else:
                    print_red("Error: Invalid option. please try again")

    elif choice == "3":
        print_green("Thank you for using Fund Flow. Goodbye!\n")
        break
    else:
        print_red("Error: Invalid option. please try again\n")
