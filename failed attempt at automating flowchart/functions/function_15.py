def input_bool(question: str):
    while True:
        user_input = input(question).strip()
        if user_input.lower() == "y":
            return True
        elif user_input.lower() == "n":
            return False
        else:
            print("Please answer in y or n. ", end="")

