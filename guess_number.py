def GUESSNUMBER():
    import random
    print("\n          WELCOME TO GUESSNUMBER          \n\n")
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
            playagain = input("Wanna play again?\n")
            if playagain == "yes":
                GUESSNUMBER()
            else:
                break
