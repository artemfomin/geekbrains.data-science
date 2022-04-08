def request_number(message: str) -> int:
    while True:
        user_input = input(message)
        if user_input.isnumeric():
            return int(user_input)
        else:
            print("Doesn't look like a number. Let's try again")


def request_alternative(message: str) -> bool:
    while True:
        user_input = input(message)
        if user_input == 'Y' or user_input == 'y':
            return True
        elif user_input == 'N' or user_input == 'n':
            return False
