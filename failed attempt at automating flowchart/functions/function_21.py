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

