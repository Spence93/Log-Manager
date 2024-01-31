
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


# def branch_list():
#     print("-" * 75)
#     print("\nBranch List:")
#     for i, logs in enumerate(log_files, 1):
#         print(i, ": ", logs.strip(".txt"))
#     print("Please choose which branch's logs you wish to open")
#     print("Press 'n' to return to main menu")


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


# def user_input_validation(prompt):
#     while True:
#         user_input = input(prompt)
#         if user_input.isnumeric():
#             user_input = int(user_input)
#             if user_input > 0 <= len(log_files):  # changed 'and user_input'
#                 break
#             else:
#                 print("Please enter a valid option")
#                 continue
#         elif user_input.lower() == "n":
#             return user_input
#         else:
#             print("Please enter a valid option")
#             continue
#     return user_input

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
    print(f"\nDATE: {clean[city_log][0]}\nSTATUS: {clean[city_log][1]}\nORDER NO: {\
          clean[city_log][2]}\nBRANCH: {clean[city_log][3]}\nDEPARTMENT: {clean[city_log][4]}")

home_page = ("\nHyperion Enterprises") + ("\nShipping Log Manager")
branch = "Branch List:"
menu_list = ["View shipping Log List",
             "Search for a Shipping Log",
             "Exit Program"]
log_files = ["London.txt", "Manchester.txt", "Glasgow.txt"]
branches = ["London", "Manchester", "New York"]
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
                    print_london = read_log(log_files[0])
                    # cleans the list of unwanted chars and creates 2D list
                    clean = list_clean(print_london)
                    # sub_list = False
                    # while (not sub_list):
                    log_input = list_logs("London", clean, log_files)

                    # edit list logs function or menu_input function??!?!!
                    # london_logs = user_input_validation("--> ") 
                
                    if log_input != "n":
                        print_log(log_input)
                        if input("\nPress any key to return "):
                            break
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
        pass

    elif main_input == 3:
        print("Exiting program, Goodbye")
        main_menu == False
        break
