from choosing_game import ChoosingGame

if __name__ == "__main__":
    while True:
        WannaPlay = input("Wanna play a game?\n").lower()
        if WannaPlay == "yes":
            input("Good choice.\nWhat game do you want to play?\n")
            NoChoice = input(
                "\nI'm joking. It's not up to you. You can play:\n \n-> HANGMAN\n \n-> GUESSNUMBER\n \n-> RPS(rock/paper/scissors)\n\nWhat's your choice?\n").lower()
            ChoosingGame(NoChoice)
            break
        else:
            continue
