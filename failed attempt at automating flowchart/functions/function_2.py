def add_new_user(admin_only=False):
    if admin_only:
        user_type = "admin"
    else:
        while True:
            print(
                """
Please select a user type from the list.
    1 = admin
    2 = inventory-checker
    3 = purchaser
        """
            )
            user_type_choice = input_int("Please select a user type: ")
            if user_type_choice == 1:
                user_type = "admin"
                break
            elif user_type_choice == 2:
                user_type = "inventory-checker"
                break
            elif user_type_choice == 3:
                user_type = "purchaser"
                break
            else:
                print("Invalid choice, please try again.\n")
    username = input_str("Enter username for the new user: ")
    password = input_str("Enter password for the new user: ")
    password_comfirmation = input_str("Enter password again: ")

    if password == password_comfirmation:
        userdata = read_csv_as_list("userdata.txt")
        for user in userdata:
            if username in user[0]:
                print("Username is already used.")
                return

        userdata.append([username, password, user_type])
        write_list_to_csv("userdata.txt", userdata)
    else:
        print("Passwords don't match. Please try again.")


# user interfaces for each user type