def input_str(question: str):
    while True:
        user_input = input(question).strip()
        if "," in user_input:
            print("',' is an invalid character. ", end="")
        else:
            return user_input

