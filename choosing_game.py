from hangman import HANGMAN
from another_game import AnotherGame
from rps import RPS
from guess_number import GUESSNUMBER


def ChoosingGame(NoChoice):
    sure = "Are you sure?\n"
    hm = "Let's play HANGMAN!"
    bs = "Let's play RPS"
    gn = "Let's play GUESSNUMBER!"
    tl = "Too late!"
    while True:
        if NoChoice == "hangman":
            Sure = input(sure).upper()
            if Sure == "YES":
                print(hm)
                HANGMAN()
                AnotherGame()
            else:
                print(tl)
                print(hm)
                HANGMAN()
                AnotherGame()
            break
        elif NoChoice == "rps" or NoChoice == "rockpaperscissors":
            Sure = input(sure).upper()
            if Sure == "YES":
                print(bs)
                RPS()
                AnotherGame()
            else:
                print(tl)
                print(bs)
                RPS()
                AnotherGame()
            break
        elif NoChoice == "guess number" or NoChoice == "guessnumber":
            Sure = input(sure).upper()
            if Sure == "YES":
                print(gn)
                GUESSNUMBER()
                AnotherGame()
            else:
                print(tl)
                print(gn)
                GUESSNUMBER()
                AnotherGame()
            break
        else:
            NoChoice = input(
                "Choose smart!\n").lower()
            continue
        break
