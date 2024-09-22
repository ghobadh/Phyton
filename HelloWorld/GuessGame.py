guess_count=0
guess_limit = 3
secret_number=9
while guess_count < guess_limit:
    guess_count += 1
    the_guess= int(input("Guess a number between 1 and 9!:"))

    if the_guess == secret_number:
        print("Congrats! You guessed the correct number!")
        break
    else:
        print("Wrong. Try again!")
else:
    print("Sorry, you lost!")
