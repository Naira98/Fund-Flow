from authentication import register
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
        pass
    elif choice == "3":
        print("Thank you for using Fund Flow. Goodbye!")
        break
    else:
        print('Error: Invalid option. please try again')
        print()