def list_all_items(data):
    if len(data) > 10:
        user_input = input_bool("The list can get very long, are you sure?")
        if user_input:
            print_table(data, data[1:])
    else:
        print_table(data, data[1:])


if __name__ == "__main__":
    main()
