command = ""
started=False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car is already start")
        else:
            print("The car starts")
            started=True
            continue
    elif command == "stop":
        if not started:
            print("The car is already stop")
        else:
            print("The car stops")
            started=False
            continue
    elif command == "help":
        print("""
        start - starts the car
        stop - stops the car
        quit - quits the app
        help - shows this help
        """)
    elif command == "quit":
        break
    else:
        print("Invalid command")
