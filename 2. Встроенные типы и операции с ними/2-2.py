import random

initial_list = []

# Прошу принять автогенерацию массива вместо ручного ввода - быстрее было проверять
# Количество элементов рандомное и суть задания по сути не меняется
for iteration in range(random.randint(5, 20)):
    initial_list.append(random.randint(1, 99))

print(f"Generated list of {initial_list.__len__()} random int elements")
print(initial_list)

buffer = None
for item in range(initial_list.__len__()):
    if item % 2 == 0 and item + 1 <= initial_list.__len__() - 1:
        buffer = initial_list[item]
        initial_list[item] = initial_list[item + 1]
        initial_list[item + 1] = buffer

print("Reordered each pair in the list")
print(initial_list)
