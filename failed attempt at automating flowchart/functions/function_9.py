def print_table(data, data_to_print):
    column_lengths = [
        max(len(str(row[col])) for row in data) for col in range(len(data[0]))
    ]

    print_row(data[0], column_lengths)
    print_separator(column_lengths)

    for row in data_to_print:
        print_row(row, column_lengths)

