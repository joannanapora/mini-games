
import random


def RPS():
    first_time = True

    while True:
        if not first_time:
            playagain = input("Wanna play again?\n").upper()
        else:
            playagain = "YES"
            first_time = False

        if playagain == "YES":
            print(
                "\n          WELCOME TO ROCK - PAPER - SCISSORS! Who gets 3 points - WIN!          \n\n")
            game()
        else:
            break


def weapones_points(p_p, c_p, player1, computer):
    print("Player: ", player1, "Computer: ", computer)
    print("------------->POINTS<--------------")
    print("Player: ", p_p, " points ||| Computer: ", c_p)
    print("-----------------------------------")


def game():
    rock = "ROCK"
    paper = "PAPER"
    scissors = "SCISSORS"

    p_p = 0
    c_p = 0
    while True:
        if p_p == 3:
            print("*******You won!*******")
            break
        if c_p == 3:
            print("*******You lost!*******")
            break
        player1 = input(
            "              What is your weapon? ROCK / PAPER / SCISSORS\n").upper()
        computer = random.choice([rock, paper, scissors])
        if player1 == computer:
            print("\nTIE!\n")
            weapones_points(p_p, c_p, player1, computer)
        if player1 == scissors:
            if computer == paper:
                p_p = p_p + 1
                weapones_points(p_p, c_p, player1, computer)
            if computer == rock:
                c_p = c_p + 1
                weapones_points(p_p, c_p, player1, computer)
        if player1 == paper:
            if computer == scissors:
                c_p = c_p + 1
                weapones_points(p_p, c_p, player1, computer)
            if computer == rock:
                p_p = p_p + 1
                weapones_points(p_p, c_p, player1, computer)
        if player1 == rock:
            if computer == paper:
                c_p = c_p + 1
                weapones_points(p_p, c_p, player1, computer)
            if computer == scissors:
                p_p = p_p + 1
                weapones_points(p_p, c_p, player1, computer)
