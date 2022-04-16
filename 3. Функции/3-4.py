import random


def validate_number_is_negative(number: int):
    if number >= 0:
        raise Exception("The power should be negative")


# my_func in my opinion is not the best and readable name
def negative_pow_custom(a: float, b: int) -> float:
    validate_number_is_negative(b)
    result = a
    for p in range(1, abs(b)):
        result = result * a
    return 1 / result


# my_func in my opinion is not the best and readable name
def negative_pow_builtin(a: float, b: int) -> float:
    validate_number_is_negative(b)
    return a ** b


input_number = random.uniform(-100, 100)
power = random.randint(-10, -2)

print(input_number)
print(power)

print(f"Built in operator result:\t{input_number} in power {power} is {negative_pow_builtin(input_number, power)}")
print(f"Custom power function result:\t{input_number} in power {power} is {negative_pow_custom(input_number, power)}")

# Sometimes when number is negative and power is negative results slightly differ
# Will investigate later
print(negative_pow_builtin(input_number, power) == negative_pow_custom(input_number, power))
