def read_csv_as_list(filename):
    with open(filename, "r") as f:
        file_text = f.read()
        f.close()
        list_of_lines = file_text.split("\n")
        inventory = []
        for line in list_of_lines:
            if not line == "":
                inventory.append(line.split(","))
    return inventory

