
# combined user input validation and menu's into one function.
def menu_inputs(menus, log_length, log_list):
    """
    The function `menu_inputs` displays a menu, lists options, and prompts the user to choose an option
    or return.

    :param menus: The `menus` parameter in the `menu_inputs` function is a string that represents the
    menu options available for the user to choose from. It is displayed at the beginning of the menu
    interface to guide the user on available options
    :param log_length: The `log_length` parameter in the `menu_inputs` function is likely intended to
    represent the total number of items in the `log_list`. It is used to validate the user input when
    choosing an option from the menu. The function checks if the user input is a numeric value within
    the range of
    :param log_list: The `log_list` parameter in the `menu_inputs` function seems to be a list of items
    that will be displayed as options in the menu. Each item in the `log_list` will be printed with a
    corresponding index number for the user to choose from
    :return: The function `menu_inputs` returns the user's selected option from the menu as an integer
    if it is a valid numeric option within the range of log_length. If the user inputs 'n', the function
    breaks out of the loop. If the user inputs an invalid option, an error message is displayed, and the
    loop continues until a valid option is chosen. If the user input is neither a valid
    """
    print("-" * 75)
    print(menus)
    print("-" * 75)
    for i, menu in enumerate(log_list, 1):
        print(i, ": ", menu)
    print("Press 'n' to return")
    while True:
        u_input = input("Please choose an option from the menu\n --> ")
        if u_input.isnumeric() and 0 < int(u_input) <= len(log_length):
            return int(u_input)
        elif u_input.lower() == "n":
            break
        else:
            print("Error not a valid option")
            continue
    return u_input


def list_logs(branch, clean_list, log_length):
    """
    The function `list_logs` displays a list of logs for a specific branch and allows the user to choose
    a log to open or return.

    :param branch: The `branch` parameter in the `list_logs` function seems to represent the branch name
    for which the logs are being displayed. It is used to specify the branch whose logs will be shown in
    the output
    :param clean_list: The `clean_list` parameter seems to be a list of lists where each inner list
    contains information about logs. Each inner list seems to have at least three elements, with the
    first element being the date and the third element being the log message
    :param log_length: The `log_length` parameter seems to represent the total number of logs available
    in the `clean_list`. It is used to validate the user input when choosing a log to open. The function
    ensures that the user input is a valid numeric option within the range of available logs or 'n' to
    return
    :return: The function `list_logs` returns the index of the log chosen by the user if a valid numeric
    option is selected, or it returns the string "n" if the user chooses to return. If an invalid option
    is entered, the function will continue prompting the user until a valid option is selected.
    """
    while True:
        print("-" * 75)
        print(f"{branch} Branch Logs: ")
        print("-" * 75)
        for i, dates in enumerate(clean_list, 1):
            print(i, ": ", dates[0], dates[2])
        print("Press 'n' to return")
        choose_log = input("Please choose which log you wish to open\n--> ")
        if choose_log.isnumeric() and 0 < int(choose_log) <= len(log_length):
            return int(choose_log)
        elif choose_log.lower() == "n":
            break
        else:
            print("enter a valid option")
            continue
    return choose_log


def read_log(city):
    """
    The function `read_log` reads the contents of a log file for a specified city and returns the log
    entries as a list of strings.

    :param city: The `read_log` function takes a parameter `city`, which is the name of the log file to
    be read. The function opens the specified log file in read mode, reads all the lines from the file,
    and returns them as a list of strings
    :return: The function `read_log(city)` reads the contents of a log file for a specific city and
    returns a list of strings, where each string represents a line in the log file.
    """
    with open(city, "r") as file:
        city_log = file.readlines()
        return city_log


def list_clean(list):
    """
    The function `list_clean` takes a list of strings, removes leading and trailing whitespaces from
    each string, and splits each string by the "|" character to create a new list of lists.

    :param list: The `list_clean` function takes a list as input and cleans each element by removing any
    leading or trailing whitespaces. It then splits each element by the "|" character and appends the
    resulting list to a new list. Finally, it returns the new list with cleaned and split elements
    :return: The function `list_clean` takes a list as input, strips any leading or trailing whitespace
    from each element, splits each element by the "|" character, and returns a new list containing the
    split elements.
    """
    new_list = []
    for i in list:
        x = i.strip()
        new_list.append(x.split("|"))
    return new_list


def find_log(clean_list):
    """
    The function `find_log` takes a list of lists as input, prompts the user to enter an order number to
    find within the list, and returns the sublist(s) containing the order number if found.

    :param clean_list: The function `find_log` takes a list of lists called `clean_list` as input. Each
    inner list in `clean_list` represents a log entry, and the function allows the user to search for a
    specific log entry by entering a 6-digit order number
    :return: The function `find_log` returns either the user input if it is 'n' (indicating the user
    wants to return) or a list of logs that contain the order number entered by the user.
    """
    while True:
        temp_list = []
        print("-" * 75)
        user_find = input(
            "Please enter the order number you wish to find\nPress 'n' to return\n -->  ")
        user_find = user_find.strip()
        print("-" * 75)
        if user_find.isnumeric() and len(user_find) == 6:
            for i in clean_list:
                for x in i:
                    if user_find in x:
                        temp_list.append(i)
                        break
                    continue
            if temp_list == []:
                print("Log not found")
                continue
        elif user_find.lower() == "n":
            return user_find
        else:
            print("Please enter a valid log number,\
    must be 6 digits long")
            continue
        return temp_list


#  ----------------- Print Functions --------------------
def print_log(city_log, clean_list):
    """
    The function `print_log` takes a city log as input and prints the corresponding date, status, order
    number, branch, and department.

    :param city_log: The parameter `city_log` is used to specify the index of the log entry in the
    `clean` list that we want to print
    """
    city_log -= 1
    print(f"""\nDATE: {clean_list[city_log][0]}\nSTATUS: {clean_list[city_log][1]}\nORDER NO: {
          clean_list[city_log][2]}\nBRANCH: {clean_list[city_log][3]}\nDEPARTMENT: {clean_list[city_log][4]}""")


def print_search(search_list):
    """
    The function `print_search` takes a list of search results and prints specific information based on
    the first element of the list.

    :param search_list: The `print_search` function takes a `search_list` as input, which seems to be a
    list of lists where each inner list contains information related to a search result. The function
    then prints out specific elements from the first inner list in a formatted way
    """
    search_input = 0
    print(f"""\nDATE:\t\t {search_list[search_input][0]}\nSTATUS:\t\t{search_list[search_input][1]}\nORDER NO:\t{
          search_list[search_input][2]}\nBRANCH:\t\t{search_list[search_input][3]}\nDEPARTMENT:\t{search_list[search_input][4]}""")


home_page = ("\nHyperion Enterprises") + ("\nShipping Log Manager")
branch = "Search for shipping log\nBranch List:"
menu_list = ["View shipping Log List",
             "Search for a Shipping Log",
             "Exit Program"]
log_files = ["London.txt", "Manchester.txt", "Glasgow.txt"]
branches = ["London", "Manchester", "Glasgow"]
main_menu = False


while (not main_menu):
    main_input = menu_inputs(home_page, log_files, menu_list)

    # View shopping Logs from a list
    if main_input == 1:
        while True:
            # Prints branch options, and returns users input
            branch_input = menu_inputs(branch, log_files, branches)
            if branch_input == "n":
                break

            # If user selects view London Logs
            if branch_input == 1:
                while True:
                    # opens file to read and store as list
                    print_london = read_log(log_files[0])
                    # cleans the list of unwanted chars and creates 2D list
                    clean_london = list_clean(print_london)
                    london_log_input = list_logs(           # Lists all logs in the london.txt file, returns users choice to view
                        "London", clean_london, log_files)
                    if london_log_input != "n":              # if user selects a valid option - the log is printed out
                        print_log(london_log_input, clean_london)
                        if input("\nPress 'n' to return "):
                            continue
                    break

            # Manchester option 2
            elif branch_input == 2:
                while True:
                    print_manch = read_log(log_files[1])
                    clean_manch = list_clean(print_manch)
                    manch_log_input = list_logs(
                        "Manchester", clean_manch, log_files)
                    if manch_log_input != "n":
                        print_log(manch_log_input, clean_manch)
                        if input("\nPress 'n' to return "):
                            continue
                    break

            # Glasgow option 3
            elif branch_input == 3:
                while True:
                    print_glas = read_log(log_files[2])
                    clean_glas = list_clean(print_glas)
                    glas_log_input = list_logs(
                        "Glasgow", clean_glas, log_files)
                    if glas_log_input != "n":
                        print_log(glas_log_input, clean_glas)
                        if input("\nPress 'n' to return"):
                            continue
                    break
    # User search function for a specific log by branch and order number.
    elif main_input == 2:
        while True:
            # Prints branch otions, and returns users choice
            s_input = menu_inputs(branch, log_files, branches)
            if s_input == "n":      # break loop to return to previous menu
                break
            # User input indexes the correct Branches .txt file for reading
            search_branch = read_log(log_files[s_input - 1])
            # branch.txt file is cleaned into the desired format
            search_clean = list_clean(search_branch)

            while True:
                # user input to search for the logs Order number
                search_result = find_log(search_clean)
                if search_result != "n":
                    print_search(search_result)
                    if input("\nPress 'n' to return "):
                        continue
                break

    elif main_input == 3:
        print("Exiting program, Goodbye")
        main_menu == False
        break
