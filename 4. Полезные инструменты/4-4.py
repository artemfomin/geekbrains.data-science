from utils.randomize import generate_random_int_list

random_numbers = generate_random_int_list(20, 1, 10)
print([num for num in list(dict.fromkeys(random_numbers))])
