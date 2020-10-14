def HANGMAN():
    import random
    print("\n          WELCOME TO HANGMAN          \n\n")
    WordsChoice = ["SAW", "DEATH", "MASACRE", "BLOOD", "FEAR", ]
    word = random.choice(WordsChoice)
    guessed = "_" * len(word)
    wholeword = word
    word = list(word)
    guessed = list(guessed)
    guessed_letters = []
    chances = 6

    def hang_pic(chances):
        print("   ------\n   |    |\n   o    |\n  /|\   |\n   /\\   |\n        ^\n")
        print("\nChances left: ", chances)

    # TODO
    # Refactor - hangman call himself, causing looping
    while True:
        print(' '.join(guessed), "\n")
        letter = input("guess letter: ").upper()
        # User check whole word:
        if len(letter) > 1:
            if letter == wholeword:
                print("You won!!")
                playagain = input("Wanna play again?\n").upper()
                if playagain == "YES":
                    HANGMAN()
                else:
                    print('Im breaking')
                    break
            else:
                print("You are wrong! Keep going!")
                chances = chances - 1
                hang_pic(chances)
                continue
        if letter.upper() in guessed_letters:
            print("You already tried this letter!")
        elif letter.upper() in word:
            while letter.upper() in word:
                index = word.index(letter.upper())
                guessed[index] = letter.upper()
                word[index] = '_'
            guessed_letters.append(letter.upper())
        else:
            if letter.upper() not in word:
                guessed_letters.append(letter.upper())
                chances = chances - 1
                hang_pic(chances)
        if '_' not in guessed:
            print("You won!!")
            playagain = input("Wanna play again?\n").upper()
            if playagain == "YES":
                HANGMAN()
            else:
                break

        if chances == 0:
            print("YOU LOST! THE WORD WAS: ", wholeword, "\n")
            playagain = input("Wanna play again?\n").upper()
            if playagain == "YES":
                HANGMAN()
            else:
                break
