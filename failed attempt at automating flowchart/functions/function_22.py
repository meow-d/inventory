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