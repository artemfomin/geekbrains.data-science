import random
from utils.randomize import generate_random_int_list

random_numbers = generate_random_int_list(10)
print([item for index, item in enumerate(random_numbers) if index > 0 and random_numbers[index] > random_numbers[index - 1]])
