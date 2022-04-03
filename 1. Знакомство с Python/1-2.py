import datetime

print("Hello again")
print("Let's play with time a bit")


def request_seconds_input():
    while True:
        input_seconds = input("Input random amount of seconds\n")
        if input_seconds.isnumeric():
            return int(input_seconds)
        else:
            print("I mean please input a valid integer number. Let's try again..")


seconds_amount = request_seconds_input()
print(seconds_amount)
print(f"This amount of seconds is {datetime.timedelta(seconds=seconds_amount)}")
