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
    print("\nBranch List:")
    for i, logs in enumerate(log_files, 1):
        print(i, ": ", logs.strip(".txt"))
    print("Please choose which branch's logs you wish to open")
    print("Press 'n' to return to main menu")


def list_dates(clean_list):
    print("\nLondon Branch Logs: ")
    for i, dates in enumerate(clean_list, 1):  
        print(i,": ", dates[0], dates[2] )
    print("Please choose which log you wish to open")
    print("Enter 'n' to return to previous menu")    


# merge input functions into one?
def first_input():
    while True:
        input_one = input("--> ")
        if input_one.isnumeric():
            input_one = int(input_one)
            if input_one > 0 and input_one <= len(menu_list):
                break
            else:
                print("Please enter a valid option")
                continue
        else:
            print("Please enter a valid option")
            continue
    return input_one        


def branch_input():
    while True:
        input_two = input("--> ")
        if input_two.isnumeric():
            input_two = int(input_two)
            if input_two > 0 and input_two <= len(log_files):
                break
            else:
                print("Please enter a valid option")
                continue
        else:
            print("Please enter a valid option")
            continue
    return input_two 


def choose_log():
    while True:
        input_three = input("--> ")
        if input_three.isnumeric():
            input_three = int(input_three)
            if input_three > 0 and input_three <= len(clean):
                break
            else:
                print("Please enter a valid option")
                continue
        elif input_three.lower() == "n":
            return input_three            
        else:
            print("Please enter a valid option")
            continue
    return input_three


def exit_log():
    while True:
        input_four = input("-->: ")
        if input_four.lower() == "y":
            break            
        else:
            sub_list = True
            return sub_list        

def read_london():
    with open(london, "r") as file:
        london_log = file.readlines()
        return london_log
    

def list_clean(list):
    new_list = []
    for i in list:
        x = i.strip( )
        new_list.append(x.split("|"))     
    return new_list  


def print_log(open_log):
        open_log -= 1
        print(f"\nDATE: {clean[open_log][0]}\nSTATUS: {clean[open_log][1]}\nORDER NO: {clean[open_log][2]}\nBRANCH: {clean[open_log][3]}\nDEPARTMENT: {clean[open_log][4]}")
        print("\nType 'y' to exit current log")



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
    main_input = first_input()

    # add while loop to take back to branch menu??

    # If statement to check user input and move to the Branch List menu
    # Another input function for user to select which Branch's log they 
    # would like to acess
    while (not logs):

        if main_input == 1:
            log_list()
            log_input = branch_input()

            # If statement used to select London branches logs
            # sub_list variable used to reset while loop, so user can re enter.
            if log_input == 1:
                print_london = read_london()
                clean = list_clean(print_london)
                sub_list = False    

                # While loop used to display the London branch logs, and give the user a choice
                # of which log they wish to view in full
                while (not sub_list):
                    log_dates = list_dates(clean)
                    open_log = choose_log()

                    # usese the input stored in open_log to open the chosen log 
                    if open_log != "n":
                        print_log(open_log)
                        exit_log() 

                    # Allows user to exit from this menu (loop) and go back to main menu                 
                    else:    
                        sub_list = True
                    

        elif main_input == 2:
            pass       

        elif main_input == 3:
            print("Exiting program, Goodbye")
            main_menu == False
            break
