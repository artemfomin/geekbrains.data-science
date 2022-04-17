import random


def generate_random_int_list(count: int, start: int = 0, end: int = 99) -> list:
    return [random.randint(start, end) for _ in range(count)]
