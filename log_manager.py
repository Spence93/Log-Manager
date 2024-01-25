def main_screen():
    print("-" * 75)
    print("Hyperion Enterprises")
    print("Shipping Log Manager")
    print("-" * 75)
    for i , menu in enumerate(menu_list, 1):
        print(i ,": ", menu)
    print("Please choose an option from the menu")

def log_list():
    print("Shipping Log List")
    for i, logs in enumerate(log_files, 1):
        print(i, ": ", logs)




main_menu = False
menu_list = ["View shipping Log List", "Search for a Shipping Log", "Exit Program"]
log_files = ["London.txt", "Manchester.txt", "Glasgow.txt"]




while (not main_menu):
    main_screen()

    while True:
        main_input = input(": ")
        if main_input.isnumeric():
            main_input = int(main_input)
            if main_input > 0 < 3:
                break
            else:
                print("Invalid option, please choose again")
        else:
            print("Please enter a valid option")
            continue

        

    if main_input == 1:
        print("-" *75)
        log_list()
        log_input = input("Please choose from the menu if you wish to open a log: ")



    elif main_input == 3:
        print("Exiting program, Goodbye")
        main_menu == False
        break