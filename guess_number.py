
import random


def GUESSNUMBER():
    first_time = True

    while True:
        if not first_time:
            playagain = input("Wanna play again?\n").upper()
        else:
            playagain = "YES"
            first_time = False

        if playagain == "YES":
            print("\n          WELCOME TO GUESSNUMBER          \n\n")
            game()
        else:
            break


def game():
    number = random.randint(0, 100)

    while True:
        choice = int(input("Guess my number between 0 and 100: "))
        if choice > number:
            print("No, my number is lower")
            continue
        elif choice < number:
            print("No, my number is higher")
            continue
        else:
            print("\nYes, this is my number, YOU WON!\n")
            break
