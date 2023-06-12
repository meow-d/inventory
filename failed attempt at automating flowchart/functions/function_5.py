def purchaser_user_interface(inventory):
    while True:
        print(
            """
Please input a number from the list to choose an operation.
    1 = replinish stock
    2 = view replenish list
    3 = search item
    4 = list all items
    9 = exit without saving changes
    0 = exit, saving changes"""
        )
        user_input = input_int("Please select a command: ")
        print(user_input)
        if user_input == 1:
            stock_replenish(inventory)
        elif user_input == 2:
            view_replenish_list(inventory)
        elif user_input == 3:
            search_items(inventory)
        elif user_input == 4:
            list_all_items(inventory)
        elif user_input == 9:
            user_input = input("are you sure you want to exit WITHOUT SAVING? [y/n]: ")
            if user_input.lower() == "y":
                break
            if user_input.lower() == "n":
                print("...")
            else:
                print("please answer in y or n")
        elif user_input == 0:
            user_input = input(
                "are you sure you want to exit WHILE SAVING ALL THE CHANGES YOU MADE? [y/n]: "
            )
            if user_input.lower() == "y":
                write_list_to_csv("inventory.txt", inventory)
                break
            if user_input.lower() == "n":
                print("...")
            else:
                print("please answer in y or n")
        else:
            print("Invalid input.")
        print()


# init