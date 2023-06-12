def input_float(question: str):
    while True:
        user_input = input(question)
        try:
            user_input = float(user_input.strip())
        except:
            print("Please input an number. ", end="")
        else:
            return user_input

