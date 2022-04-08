from utils.input import request_number

months_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

months_list = [ "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December" ]

number = None
while True:
    number = request_number("Please enter month number (from 1 to 12)\n")
    if number < 1 or number > 12:
        print(f"{number} doesn't correspond with a number of the month. Try again")
    else:
        break

print(f"From dictionary:\t\tMonth number {number} is {months_dict[number]}")
print(f"From list:\t\t\tMonth number {number} is {months_list[number - 1]}")
