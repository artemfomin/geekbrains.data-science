user_input = input("Please type several words divided by whitespace\n")

word_list = user_input.split()

for index, word in enumerate(word_list, 1):
    print(f"{index}.\t{word[:10]}")