print("Hey, this task might look strange, but we have what we have")


def request_digit():
    while True:
        user_input = input("Please enter a DIGIT:\n")
        if user_input.isnumeric() and len(user_input) == 1:
            return int(user_input)
        else:
            print("I mean enter ONE DIGIT. Doesn't look like what you've entered. Let's try again")


def find_strange_number(number: int, times: int):
    if not (isinstance(number, int) and isinstance(times, int)):
        raise TypeError
    strange_number = 0
    strange_result = 0
    for i in range(times):
        strange_number += (10 ** i) * number
        strange_result += strange_number
    return strange_result


digit = request_digit()
result = find_strange_number(digit, 3)

print(f"The strange number that we need in this task is {result}")
