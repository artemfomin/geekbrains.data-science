print("Let's do some sports, ha?")


def request_number(message: str) -> int:
    while True:
        user_input = input(message)
        if user_input.isnumeric():
            return int(user_input)
        else:
            print("Doesn't look like a number. Let's try again")


initial_result = request_number("What is runner's first day result?\n")
expected_result = request_number("What is the expected result?\n")

if expected_result <= initial_result:
    print("Not funny. He already did it")
else:
    day = 1
    while True:
        if day == 1:
            pass
        else:
            initial_result += initial_result / 100 * 10
            print(f"Day {day} result: {round(initial_result, 2)}")
        if initial_result >= expected_result:
            print(f"Runner will achieve expected result on day {day}")
            break
        else:
            day += 1
