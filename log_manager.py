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


def read_london():
    with open(london, "r") as file:
        london_log = file.readlines()
        return london_log
    

def list_clean(list):
    new_list = []
    for i in list:
        new_list.append(i.strip( ))
        
    for e , log in enumerate(new_list, 1): 
        print(e,": ", log)  

    



main_menu = False
menu_list = ["View shipping Log List",
             "Search for a Shipping Log", 
             "Exit Program"]
log_files = ["London.txt", "Manchester.txt", "Glasgow.txt"]
london = "London.txt"


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
            print_london = read_london()
            clean = list_clean(print_london)
            print(clean)

    elif main_input == 3:
        print("Exiting program, Goodbye")
        main_menu == False
        break
