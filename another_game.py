from hangman import HANGMAN
from guess_number import GUESSNUMBER
from rps import RPS


def AnotherGame():
    while True:
        another_game = input("Would you like to play another game?\n").lower()
        if another_game == "yes":
            games = input(
                "\nYou can play:\n \n-> HANGMAN\n \n-> GUESSNUMBER\n \n-> RPS(rock/paper/scissors)\n\nWhat's your choice?\n").lower()
            if games == "hangman":
                HANGMAN()
            elif games == "guessnumber" or games == "guess number":
                GUESSNUMBER()
            elif games == "rps" or games == "rockpaperscissors":
                RPS()
        else:
            print("Bye, then!")
            break
