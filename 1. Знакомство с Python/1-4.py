print("Let's find the biggest digit in integer")


def request_positive_integer():
    while True:
        user_input = input("Please input positive integer number\n")
        if user_input.isnumeric() and int(user_input) >= 0:
            user_input = int(user_input)
            max_number = 0
            while user_input >= 1:
                last_digit = user_input % 10
                user_input = int((user_input - last_digit) / 10)
                if last_digit > max_number:
                    max_number = last_digit
            return max_number
        else:
            print("I mean INTEGER and POSITIVE number. Be careful. Let's try again")


max_number_from_input = request_positive_integer()
print(f"Maximum digit in your input is {max_number_from_input}")
