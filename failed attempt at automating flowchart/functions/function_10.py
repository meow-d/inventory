def print_row(row, column_lengths):
    for col, value in enumerate(row):
        print("|", str(value).ljust(column_lengths[col]), end=" ")
    print("|")

