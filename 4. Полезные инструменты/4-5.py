import itertools
import operator
from functools import reduce

gen = [num for num in range(100, 1001) if num % 2 == 0]
print(reduce(lambda x, y: x * y, gen))                          # V1
print(list(itertools.accumulate(list(gen), operator.mul))[-1])  # V2
