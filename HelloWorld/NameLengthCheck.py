name = input("What is your name?")
if len(name) < 3:
    print("Your name must be at least 3 characters long.")
elif len(name) > 50:
    print("Your name must be at most 50 characters long.")
else:
    print("Your name was successfully entered.")
