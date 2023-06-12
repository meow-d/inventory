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