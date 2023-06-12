def take_stock(data: list):
    if len(data) == 1:
        print("There are no items in the database.")
    else:
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