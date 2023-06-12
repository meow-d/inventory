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

