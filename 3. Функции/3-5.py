def is_valid_number(custom_string: str) -> bool:
    return custom_string.isnumeric() or \
           (custom_string[0] == "-" and custom_string[-(len(custom_string) - 1):].isnumeric())


def contains_number(custom_string: str) -> bool:
    return any(x.isnumeric() for x in custom_string)


def contains_special_char(custom_string: str) -> bool:
    return any(not (x.isalnum() or (x == "-" and custom_string.index(x) == 0)) for x in custom_string)


def starts_with_special_char(custom_string: str) -> bool:
    return custom_string[0] != "-" and not custom_string[0].isalnum()


def extract_number(custom_string: str) -> int:
    result = ""
    for char in custom_string:
        if char.isnumeric() or (custom_string.index(char) == 0 and char == "-"):
            result = result + char
        else:
            break
    return int(result)


def request_string_of_numbers(existing_sum: int = 0) -> (bool, int):
    input_array = input("Please enter string with numbers divided by whitespaces\n").split()
    for item in input_array:
        if is_valid_number(item):
            existing_sum = existing_sum + int(item)
        elif contains_special_char(item) and not starts_with_special_char(item) and contains_number(item):
            existing_sum = existing_sum + extract_number(item)
            return False, existing_sum
        elif contains_special_char(item) and starts_with_special_char(item):
            return False, existing_sum
        else:
            print("Don't understand input. Try again")
    print(f"Current sum is {existing_sum}")
    return True, existing_sum


final_result = 0


while True:
    current_result = request_string_of_numbers(final_result)
    final_result = current_result[1]
    if not current_result[0]:
        break

print(f"FINAL RESULT IS {final_result}")
