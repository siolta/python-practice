from random import randrange


def hangman(word):
    wrong = 0
    stages = ["",
              "|________________",
              "|                ",
              "|       |        ",
              "|       O        ",
              "|      /|\\       ",
              "|      / \\       ",
              "|                "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: \n"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(board)
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))


words = ["cat", "dog", "house", "fortune"]

hangman(words[randrange(len(words))])
