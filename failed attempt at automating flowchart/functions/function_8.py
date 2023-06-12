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