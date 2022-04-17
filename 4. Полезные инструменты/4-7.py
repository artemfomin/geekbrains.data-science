import itertools
import operator


def fact(n: int):
    acum = None
    suitable_range = None

    if n == 0:
        yield 1
    elif n < 0:
        suitable_range = range(n, 0)
    else:
        suitable_range = range(1, n + 1)

    iterable = itertools.accumulate(suitable_range, operator.mul)
    for num in suitable_range:
        yield next(iterable)


for each in fact(-4):
    print(each)
