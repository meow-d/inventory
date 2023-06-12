import os
from getpass import getpass


# main functions
def main():
    first_column = [
        "Code",
        "Description",
        "Category",
        "Unit",
        "Price",
        "Quantity",
        "Minimum",
    ]
    print("Welcome to this very badly made invenvory system.")
    inventory = init(first_column)
    current_user_type = user_authentication()

    if current_user_type == "admin":
        admin_user_interface(inventory)
    elif current_user_type == "inventory-checker":
        inventory_checker_user_interface(inventory)
    elif current_user_type == "purchaser":
        purchaser_user_interface(inventory)
    else:
        print("Invalid user type. Exiting...")


## authentication
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
            user_input = input_bool("are you sure you want to exit WITHOUT SAVING? [y/n]: ")
            if user_input:
                break
        elif user_input == 0:
            user_input = input_bool(
                "are you sure you want to exit WHILE SAVING ALL THE CHANGES YOU MADE? [y/n]: "
            )
            if user_input:
                write_list_to_csv("inventory.txt", inventory)
                break
            else:
                print("...")
        elif user_input == 10:
            add_new_user()
        else:
            print("Invalid input.")
        print()


def inventory_checker_user_interface(inventory):
    while True:
        print(
            """
Please input a number from the list to choose an operation.
    1 = take stock
    2 = search item
    3 = list all items
    9 = exit without saving changes
    0 = exit, saving changes"""
        )
        user_input = input_int("Please select a command: ")
        if user_input == 1:
            take_stock(inventory)
        elif user_input == 2:
            search_items(inventory)
        elif user_input == 3:
            list_all_items(inventory)
        elif user_input == 9:
            user_input = input_bool("are you sure you want to exit WITHOUT SAVING? [y/n]: ")
            if user_input:
                break
        elif user_input == 0:
            user_input = input_bool(
                "are you sure you want to exit WHILE SAVING ALL THE CHANGES YOU MADE? [y/n]: "
            )
            if user_input:
                write_list_to_csv("inventory.txt", inventory)
                break
        else:
            print("Invalid input.")
        print()


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
            user_input = input_bool("are you sure you want to exit WITHOUT SAVING? [y/n]: ")
            if user_input:
                break
        elif user_input == 0:
            user_input = input_bool(
                "are you sure you want to exit WHILE SAVING ALL THE CHANGES YOU MADE? [y/n]: "
            )
            if user_input:
                write_list_to_csv("inventory.txt", inventory)
                break
        else:
            print("Invalid input.")
        print()


# init
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
def read_csv_as_list(filename):
    with open(filename, "r") as f:
        file_text = f.read()
        f.close()
        list_of_lines = file_text.split("\n")
        inventory = []
        for line in list_of_lines:
            if not line == "":
                inventory.append(line.split(","))
    return inventory


def write_list_to_csv(filename, data: list):
    # convert
    out = ""
    for row in data:
        row_str = map(str, row)
        out += ",".join(row_str) + "\n"

    # write
    raw_file = open(filename, "w")
    raw_file.write(out)
    raw_file.close()


# table functions
def print_table(data, data_to_print):
    column_lengths = [
        max(len(str(row[col])) for row in data) for col in range(len(data[0]))
    ]

    print_row(data[0], column_lengths)
    print_separator(column_lengths)

    for row in data_to_print:
        print_row(row, column_lengths)


def print_row(row, column_lengths):
    for col, value in enumerate(row):
        print("|", str(value).ljust(column_lengths[col]), end=" ")
    print("|")


def print_separator(column_lengths):
    for length in column_lengths:
        print("|", "-" * length, end=" ")
    print("|")


# input validation functions
def input_int(question: str):
    while True:
        user_input = input(question)
        try:
            user_input = int(user_input.strip())
        except:
            if user_input == "":
                return user_input
            print("Please input an integer. ", end="")
        else:
            return user_input


def input_float(question: str):
    while True:
        user_input = input(question)
        try:
            user_input = float(user_input.strip())
        except:
            print("Please input an number. ", end="")
        else:
            return user_input


def input_str(question: str):
    while True:
        user_input = input(question).strip()
        if "," in user_input:
            print("',' is an invalid character. ", end="")
        else:
            return user_input


def input_bool(question: str):
    while True:
        user_input = input(question).strip()
        if user_input.lower() == "y":
            return True
        elif user_input.lower() == "n":
            return False
        else:
            print("Please answer in y or n. ", end="")


def input_row_number(data, question: str):
    while True:
        row_number = input_int(question)
        if row_number == 0:
            print("Please input a number above 0. ", end="")
        elif row_number > len(data):
            print("Row does not exist")
        else:
            return row_number


# inventory-checker user functions
def take_stock(data: list):
    if len(data) == 1:
        print("There are no items in the database.")
        return

    item_row = input_row_number(data, "Which row of item do you want to update?: ")
    if item_row == 0:
        print("Please input a number above 0")
    elif item_row > len(data):
        print("Row does not exist")
    else:
        # stock column position is hardcoded
        print(f"Current stock of {data[item_row][2]} is {data[item_row][5]}.")
        user_input = input_int(
            f"Please insert new stock quantity, or leave blank to not modify data: "
        )
        data[item_row][5] = user_input


# purchaser user functions
def stock_replenish(data):
    if len(data) == 1:
        print("There are no items in the database.")
        return

    item_row = input_row_number(
        data, "Which row of item do you want to replenish?: "
    )

    # stock column position is hardcoded
    print(f"Currently stock of {data[item_row][2]}: {data[item_row][5]}")
    user_input = input_int(
        f"Please insert the amount of stock to replenish, or leave blank to not modify data: "
    )
    if user_input != "":
        data[item_row][5] = int(data[item_row][5]) + user_input


def view_replenish_list(data):
    replenish_list = []
    for item in data:
        # the positions are hardcoded
        if item[5] < item[6]:
            replenish_list.append(item)
    if len(replenish_list) > 0:
        print("Replenish list:")
        print_table(data, replenish_list)
    else:
        print("No items require replenishment.")


# admin user functions (inventory)
def insert_item(data: list):
    amount_to_insert = input_int("How many items do you want to add?: ")
    while amount_to_insert != 0:
        data.append([])
        for column_name in data[0]:
            # input data, with data validation
            if column_name == "Price":
                user_input = input_float(f"Please insert new data for {column_name}: ")
            elif column_name in ["Quantity", "Minimum", "Code"]:
                user_input = input_int(f"Please insert new data for {column_name}: ")
            else:
                user_input = input_str(f"Please insert new data for {column_name}: ")
            data[-1].append(user_input)
        amount_to_insert -= 1
    print(f"{amount_to_insert} items added successfully.")


def update_item(data: list):
    if len(data) == 1:
        print("There are no items in the database.")
    else:
        item_id = input_row_number(data, "Which row do you want to update?: ")
        print("Leave blank to not override data")
        for column_number, (column_name, column_value) in enumerate(
            zip(data[0], data[item_id])
        ):
            # input data, with data validation
            if column_name == "Price":
                user_input = input_float(
                    f"Please insert new data for {column_name} ({column_value}): "
                )
            elif column_name in ["Quantity", "Minimum", "Code"]:
                user_input = input_int(
                    f"Please insert new data for {column_name} ({column_value}): "
                )
            else:
                user_input = input_str(
                    f"Please insert new data for {column_name} ({column_value}): "
                )
            if user_input != "":
                data[item_id][column_number] = user_input
        print("Data has been updated succesfully")


def delete_item(data):
    delete_by_item_code = input_bool(
        "Do you want to delete by item code? if not, you'll have to enter the row number [y/n]: "
    )
    if delete_by_item_code:
        item_deleted = False
        code = input_str("Enter item code to delete: ")

        deletion_comfirmed = input_bool(
            f"Are you sure you want to delete item {code}? [y/n]: "
        )
        if deletion_comfirmed:
            for item in data:
                if item[0] == code:
                    data.remove(item)
                    item_deleted = True
                    break

            if item_deleted:
                print(f"Item with code {code} has been deleted.")
            else:
                print("Item not found.")

    else:
        row_number = input_row_number(data, "Enter row number to delete: ")
        deletion_comfirmed = input_bool(
            f"Are you sure you want to delete row {row_number}? [y/n]: "
        )
        if deletion_comfirmed:
            data.remove(item[row_number])
            print(f"Item with code {row_number} has been deleted.")


# search functions (accessible to everyone)
def search_items(data):
    user_input = input_int(
        """Search items by:
    1 = Description
    2 = Code range
    3 = Category
    4 = Price range
    5 = Row number range
Enter choice: """
    )

    if user_input == "1":
        description = input_str("Enter item description: ")
        found_items = []
        for item in data:
            if description.lower() in item[2].lower():
                found_items.append(item)
        if found_items:
            print("Found items:")
            print_table(data, found_items)
        else:
            print("No items found.")

    elif user_input == "2":
        range_min = input_int("Enter minimum code range: ")
        range_max = input_int("Enter maximum code range: ")
        found_items = []
        for item in data:
            if int(range_min) <= int(item[1]) <= int(range_max):
                found_items.append(item)
        if found_items:
            print("Found items:")
            print_table(data, found_items)
        else:
            print("No items found.")

    elif user_input == "3":
        category = input_str("Enter category: ")
        found_items = []
        for item in data:
            if category.lower() == item["category"].lower():
                found_items.append(item)
        if found_items:
            print("Found items:")
            print_table(data, found_items)
        else:
            print("No items found.")

    elif user_input == "4":
        price_min = input_float("Enter minimum price: ")
        price_max = input_float("Enter maximum price: ")
        found_items = []
        for item in data:
            if price_min <= item["price"] <= price_max:
                found_items.append(item)
        if found_items:
            print("Found items:")
            print_table(data, found_items)
        else:
            print("No items found.")

    elif user_input == "5":
        range_min = input_int("Enter minimum row number range: ")
        range_max = input_int("Enter maximum row number range: ")
        found_items = []
        for item in data[range_min:range_max]:
            found_items.append(item)
        if found_items:
            print("Found items:")
            print_table(data, found_items)
        else:
            print("No items found.")

    else:
        print("Please insert a number from 1 to 4", end="")
        return


def list_all_items(data):
    if len(data) > 10:
        user_input = input_bool("The list can get very long, are you sure?")
        if user_input:
            print_table(data, data[1:])
    else:
        print_table(data, data[1:])


if __name__ == "__main__":
    main()
