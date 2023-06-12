def admin_user_interface(inventory):
    while True:
        print(
            """
Please input a number from the list to choose an operation.
    1 = take stock
    2 = replinish stock
    3 = view replenish list
    4 = insert item
    5 = update item
    6 = delete item
    7 = search item
    8 = list all items
    9 = exit without saving changes
    0 = exit, saving changes
    10 = add new user account"""
        )
        user_input = input_int("Please select a command: ")
        if user_input == 1:
            take_stock(inventory)
        elif user_input == 2:
            stock_replenish(inventory)
        elif user_input == 3:
            view_replenish_list(inventory)
        elif user_input == 4:
            insert_item(inventory)
        elif user_input == 5:
            update_item(inventory)
        elif user_input == 6:
            delete_item(inventory)
        elif user_input == 7:
            search_items(inventory)
        elif user_input == 8:
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
        elif user_input == 10:
            add_new_user()
        else:
            print("Invalid input.")
        print()

