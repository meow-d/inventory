def view_replenish_list(data):
    replenish_list = []
    for item in data:
        # the positions are hardcoded
        if item[5] < item[6]:
            replenish_list.append(item)
    if len(replenish_list) > 0:
        print("Replenish list:")
        print_table(data, replenish_list)
    else:
        print("No items require replenishment.")


# admin user functions (inventory)