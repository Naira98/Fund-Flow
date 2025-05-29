from authentication import register, login
while True:
    print("╔════════════════════════════════════╗")
    print("║      Welcome to Fund Flow!         ║")
    print("║  Your personal finance companion.  ║")
    print("║                                    ║")
    print("║  1) Register                       ║")
    print("║  2) Login                          ║")
    print("║  3) Exit                           ║")
    print("╚════════════════════════════════════╝")

    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        user = login()
        if user:
            print("╔════════════════════════════════════╗")
            print("║           Projects Menu            ║")
            print("║                                    ║")
            print("║  1) Create Project                 ║")
            print("║  2) View Projects                  ║")
            print("║  3) Edit Project                   ║")
            print("║  4) Delete Project                 ║")
            print("║  5) Search Project                 ║")
            print("║  6) Logout                         ║")
            print("╚════════════════════════════════════╝")

            choice = input("Choose an option: ")

    elif choice == "3":
        print("Thank you for using Fund Flow. Goodbye!")
        break
    else:
        print('Error: Invalid option. please try again')
        print()