
# combined user input validation and menu's into one function.
def menu_inputs(menus, log_length, log_list):
    while True:
        print("-" * 75)
        print(menus)
        print("-" * 75)        
        for i, menu in enumerate(log_list, 1):
            print(i, ": ",menu)
        print("Press 'n' to return")    
        u_input = input("Please choose an option from the menu\n --> ")
        if u_input.isnumeric() and 0 < int(u_input) <= len(log_length):
            return int(u_input)
        elif u_input.lower() == "n":
            break
        else:
            print("enter a valid option")
            continue
    return u_input


def list_logs(branch, clean_list, log_length):
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
    with open(city, "r") as file:
        city_log = file.readlines()
        return city_log


def list_clean(list):
    new_list = []
    for i in list:
        x = i.strip()
        new_list.append(x.split("|"))
    return new_list


def print_log(city_log, clean_list):
    """
    The function `print_log` takes a city log as input and prints the corresponding date, status, order
    number, branch, and department.

    :param city_log: The parameter `city_log` is used to specify the index of the log entry in the
    `clean` list that we want to print
    """
    city_log -= 1
    print(f"\nDATE: {clean_list[city_log][0]}\nSTATUS: {clean_list[city_log][1]}\nORDER NO: {\
          clean_list[city_log][2]}\nBRANCH: {clean_list[city_log][3]}\nDEPARTMENT: {clean_list[city_log][4]}")


def find_log (clean_list):
    while True:
        temp_list = []
        temp_list.clear()
        user_find = input("Please enter the order number you wish to find:  ")
        user_find = user_find.strip()
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
                
        else:
            print("Please enter a valid log number,\
    must be 6 digits long")
            continue        
        return temp_list


def print_search(search_list):
    search_input = 0
    print(f"\nDATE:\t\t {search_list[search_input][0]}\nSTATUS:\t\t{search_list[search_input][1]}\nORDER NO:\t{\
          search_list[search_input][2]}\nBRANCH:\t\t{search_list[search_input][3]}\nDEPARTMENT:\t{search_list[search_input][4]}")

    

home_page = ("\nHyperion Enterprises") + ("\nShipping Log Manager")
branch = "Branch List:"
menu_list = ["View shipping Log List",
             "Search for a Shipping Log",
             "Exit Program"]
log_files = ["London.txt", "Manchester.txt", "Glasgow.txt"]
branches = ["London", "Manchester", "Glasgow"]
main_menu = False
sub_list = False
logs = False


while (not main_menu):
    main_input = menu_inputs(home_page, log_files, menu_list)
  

    if main_input == 1:
        while True:
            branch_input = menu_inputs(branch, log_files, branches)
            if branch_input == "n":
                break


            if branch_input == 1:
                while True:
                    # opens file to read and store as list
                    print_london = read_log(log_files[0])
                    # cleans the list of unwanted chars and creates 2D list
                    clean_london = list_clean(print_london)
                    log_input = list_logs("London", clean_london, log_files)
                
                    if log_input != "n":
                        print_log(log_input, clean_london)
                        if input("\nPress 'n' to return "):
                            continue       
                    break        

            # New York option 2
            elif branch_input == 2:
                pass

            # Paris option 3
            elif branch_input == 3:
                pass

            # Exit
            elif branch_input == "n":
                pass# logs = True

    elif main_input == 2:

        # change function to take search_input and find relevent file in one 
        # function?
        s_input = menu_inputs(branch, log_files, branches)
        # if s_input == 1:
        search_branch = read_log(log_files[s_input -1])
        search_clean = list_clean(search_branch)
        search_result = find_log(search_clean)
        print_search(search_result)
        if input("\nPress 'n' to return "):
            continue  
        

    elif main_input == 3:
        print("Exiting program, Goodbye")
        main_menu == False
        break
