# I find function name int_func() completely
# incompatible with function content and not descriptive
def capitalize_first(text: str) -> str:
    return text.title()


input_string = input("Your word?\n")
print(capitalize_first(input_string))

input_array = input("Now try the same but with multiple words divided by whitespace").split()
print(" ".join(list(map(capitalize_first, input_array))), )
