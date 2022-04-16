import random


def my_func(a: int, b: int, c: int) -> int:
    sorted_list = sorted([a, b, c])
    return sorted_list[-1] + sorted_list[-2]


first = random.randint(0, 10)
second = random.randint(0, 10)
third = random.randint(0, 10)

print(f"Generated numbers {first}, {second} and {third}")
print(f"Sum of two biggest numbers is {my_func(first, second, third)}")
