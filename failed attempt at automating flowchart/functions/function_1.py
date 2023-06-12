def user_authentication():
    userdata = read_csv_as_list("userdata.txt")

    if not any(user[2] == "admin" for user in userdata):
        print("No admin account detected. Please create an admin account.")
        add_new_user(admin_only=True)

    while True:
        username = input_str("\nEnter username: ")
        print("(for your security, password input isn't displayed)")
        password = getpass("Enter password: ")

        for user in userdata:
            if user[0] == username and user[1] == password:
                return user[2]
        print("Incorrect username or password. Please try again.")

