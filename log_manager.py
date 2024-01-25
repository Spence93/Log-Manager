def main_screen():
    print("-" * 75)
    print("Hyperion Enterprises")
    print("Shipping Log Manager")
    print("-" * 75)
    for i, menu in enumerate(menu_list, 1):
        print(i, ": ", menu)
    print("Please choose an option from the menu")


def log_list():
    print("-" * 75)
    print("Branch List:")
    for i, logs in enumerate(log_files, 1):
        print(i, ": ", logs.strip(".txt"))
    print("Please choose which branch's logs you wish to open")


def open_london():
    with open(london, "r") as file:
        london_log = file.readlines()
        print(london_log)


main_menu = False
menu_list = ["View shipping Log List",
             "Search for a Shipping Log", "Exit Program"]
log_files = ["London.txt", "Manchester.txt", "Glasgow.txt"]
london = "london.txt"


while (not main_menu):
    main_screen()

    while True:
        main_input = input("--> ")
        if main_input.isnumeric():
            main_input = int(main_input)
            if main_input > 0 and main_input < 4:
                break
            else:
                print("Please enter a valid option")
                continue
        else:
            print("Please enter a valid option")
            continue

    if main_input == 1:
        log_list()
        log_input = int(input("--> "))
        if log_input == 1:
            open_london()

    elif main_input == 3:
        print("Exiting program, Goodbye")
        main_menu == False
        break
