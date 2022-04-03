print("Let's play a bit with finances")


def request_number(message: str) -> int:
    while True:
        user_input = input(message)
        if user_input.isnumeric():
            return int(user_input)
        else:
            print("Doesn't look like a number. Let's try again")


income = request_number("Please enter your income for the last period\n")
expenses = request_number("Please enter your expenses for the last period\n")

if expenses < income:
    print("Balance for the period is positive. Congratulations!")
    profitability = income / expenses
    print(f"Profitability for the period is {profitability}")
    employee_count = request_number("Please eneter the count of your employees\n")
    profit_per_employee = (income - expenses) / employee_count
    print(f"Profit per employee is {profit_per_employee}")
elif expenses == income:
    print("You have zero balance for the period")
else:
    print("You have negative balance for the period")
