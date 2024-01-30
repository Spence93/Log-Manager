def main_screen():
    print("-" * 75)
    print("Hyperion Enterprises")
    print("Shipping Log Manager")
    print("-" * 75)
    for i, menu in enumerate(menu_list, 1):
        print(i, ": ", menu)
    print("Please choose an option from the menu")


def branch_list():
    print("-" * 75)
    print("\nBranch List:")
    for i, logs in enumerate(log_files, 1):
        print(i, ": ", logs.strip(".txt"))
    print("Please choose which branch's logs you wish to open")
    print("Press 'n' to return to main menu")


def list_logs(clean_list):
    print("\nLondon Branch Logs: ")
    for i, dates in enumerate(clean_list, 1):
        print(i, ": ", dates[0], dates[2])
    print("Please choose which log you wish to open")
    print("Enter 'n' to return to previous menu")


def user_input_validation(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input > 0 <= len(log_files):  # changed 'and user_input'
                break
            else:
                print("Please enter a valid option")
                continue
        elif user_input.lower() == "n":
            return user_input
        else:
            print("Please enter a valid option")
            continue
    return user_input

# rename as now multiuse


def read_log(city):
    with open(city, "r") as file:
        city_log = file.readlines()
        return city_log


def list_clean(list):
    new_list = []
    for i in list:
        x = i.strip()
        new_list.append(x.split("|"))
    return new_list


def print_log(city_log):
    """
    The function `print_log` takes a city log as input and prints the corresponding date, status, order
    number, branch, and department.

    :param city_log: The parameter `city_log` is used to specify the index of the log entry in the
    `clean` list that we want to print
    """
    city_log -= 1
    print(f"\nDATE: {clean[city_log][0]}\nSTATUS: {clean[city_log][1]}\nORDER NO: {
          clean[city_log][2]}\nBRANCH: {clean[city_log][3]}\nDEPARTMENT: {clean[city_log][4]}")


menu_list = ["View shipping Log List",
             "Search for a Shipping Log",
             "Exit Program"]
log_files = ["London.txt", "Manchester.txt", "Glasgow.txt"]
main_menu = False
sub_list = False
logs = False


# Main menu and an input function for the user to select an option
while (not main_menu):
    main_screen()
    main_input = user_input_validation("--> ")

    if main_input == 1:

        logs = False
        while (not logs):
            branch_list()
            branch_input = user_input_validation("--> ")

            if branch_input == 1:
                print_london = read_log(log_files[0])
                # cleans the list of unwanted chars and creates 2D list
                clean = list_clean(print_london)

                sub_list = False
                while (not sub_list):
                    log_dates = list_logs(clean)
                    london_logs = user_input_validation("--> ")

                    # uses the input stored in london_logs to open the chosen log
                    if london_logs != "n":
                        print_log(london_logs)
                        if input("Enter any key to close "):
                            continue
                    else:
                        sub_list = True

            # New York option 2
            elif branch_input == 2:
                pass

            # Paris option 3
            elif branch_input == 3:
                pass

            # Exit
            elif branch_input == "n":
                logs = True

    elif main_input == 2:
        pass

    elif main_input == 3:
        print("Exiting program, Goodbye")
        main_menu == False
        break
