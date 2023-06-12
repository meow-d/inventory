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