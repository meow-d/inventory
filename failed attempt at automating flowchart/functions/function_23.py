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
        description = input("Enter item description: ")
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
        category = input("Enter category: ")
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

