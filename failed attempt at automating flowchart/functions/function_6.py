def init(first_column: list):
    if not os.path.exists("userdata.txt"):
        open("userdata.txt", "x")
        print("userdata.txt created. Please create an admin account.")
        add_new_user(admin_only=True)

    if not os.path.exists("inventory.txt"):
        open("inventory.txt", "x")
        print("inventory.txt created.")
        write_list_to_csv("inventory.txt", [first_column])
    return read_csv_as_list("inventory.txt")


# file functions