def input_int(question: str):
    while True:
        user_input = input(question)
        try:
            user_input = int(user_input.strip())
        except:
            print("Please input an integer. ", end="")
        else:
            return user_input

