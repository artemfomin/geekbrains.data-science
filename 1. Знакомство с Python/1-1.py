print("Hey")

name = input("What's your name?\n")
print(f"Good to meet you {name}")

age = int(input(f"How old are you, {name}?\n"))
if age < 18:
    print(f"Thanks god Python in legal for young people, {name} ;))")
elif 18 <= age < 40:
    print(f"We're more or less of the same age, {name}! You're just in time!")
elif 40 <= age < 50:
    print(f"Well, it's never too late, {name}. Ha?")
else:
    print(f"Poor {name}.. It's a miracle you're still alive, dude. However, good luck in learning Python")

print(f"Okay, {name}, good to see you anyway. Let's proceed to the next lesson")
