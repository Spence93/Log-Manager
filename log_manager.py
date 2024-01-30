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
            if user_input > 0 and user_input <= len(log_files):
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


def read_london():
    with open(london, "r") as file:
        london_log = file.readlines()
        return london_log


def list_clean(list):
    new_list = []
    for i in list:
        x = i.strip()
        new_list.append(x.split("|"))
    return new_list


def print_log(open_log):
    open_log -= 1
    print(f"\nDATE: {clean[open_log][0]}\nSTATUS: {clean[open_log][1]}\nORDER NO: {
          clean[open_log][2]}\nBRANCH: {clean[open_log][3]}\nDEPARTMENT: {clean[open_log][4]}")


main_menu = False
menu_list = ["View shipping Log List",
             "Search for a Shipping Log",
             "Exit Program"]
log_files = ["London.txt", "Manchester.txt", "Glasgow.txt"]
london = "London.txt"
sub_list = False
logs = False
# add variable to single function to select branch txt fille !!


# Main menu and an input function for the user to select an option
# sub_list var to res
while (not main_menu):
    main_screen()
    main_input = user_input_validation("--> ")

    # add while loop to take back to branch menu??

    # If statement to check user input and move to the Branch List menu
    # Another input function for user to select which Branch's log they
    # would like to acess
    if main_input == 1:
        logs = False
        while (not logs):
            # This funciton prints out the branch list and we get the user choice for
            # the menu stored in log_input
            branch_list()
            log_input = user_input_validation("--> ")

            # Option 1 run opens and cleans the London.txt file
            if log_input == 1:
                # reads the lond.txt file as readlines() - stores in list
                print_london = read_london()
                # cleans the list of unwanted chars and creates 2D list
                clean = list_clean(print_london)
                sub_list = False

                # While loop used to display the London branch logs, and give the user a choice
                # of which log they wish to view in full
                while (not sub_list):
                    log_dates = list_logs(clean)
                    open_log = user_input_validation("--> ")

                    # uses the input stored in open_log to open the chosen log
                    if open_log != "n":
                        print_log(open_log)
                        if input("Enter any key to close "):
                            break
                    else:
                        sub_list = True

            # New York option 2
            elif log_input == 2:
                pass

            # Paris option 3
            elif log_input == 3:
                pass

            # Exit
            elif log_input == "n":
                logs = True

    elif main_input == 2:
        pass

    elif main_input == 3:
        print("Exiting program, Goodbye")
        main_menu == False
        break
