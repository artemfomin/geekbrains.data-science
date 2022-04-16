import random


def divide(a: int, b: int) -> float:
    if not isinstance(a, int) or not isinstance(b, int):
        raise(TypeError("Operands should be numbers"))
    if b == 0:
        raise(ZeroDivisionError("Don't even try to divide by zero"))
    return float(a / b)


for number in range(10):
    first = random.randint(0, 20)
    second = random.randint(0, 20)
    print(f"{first} / {second} = {round(divide(first, second), 2)}")
