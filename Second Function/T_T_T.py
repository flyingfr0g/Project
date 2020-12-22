#!/usr/bin/env python3

# this is my re-creation of tic-tac-toe in python

# first we create the game spaces for the players to use. This will look very much like a number pad.

gameboard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in gameboard:
    board_keys.append(key)

# Next we start creating functions that will actually make the game playable

# The first function will print out the game board after every turn

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# Now we will create the "playable" function, giving each user a turn.
# Players will use the number pad to input their moves
# If the space is already taken or the player types an incorrect number they get an error message

def game():
    move = 'X'
    count = 0

    for i in range(10):
        printBoard(gameboard)
        print("Your move ," + move + ". which space do you want?")

        space = input()

        if gameboard[space] == ' ':
            gameboard[space] = move
            count += 1
        else:
            print("Not smoov that space is already taken.\nWhich space do you want?")
            continue

        # Now we check to see which player won!

        if count >= 5:
            if gameboard['7'] == gameboard['8'] == gameboard['9'] != ' ':  # this checks the board across the top
                printBoard(gameboard)
                print("\nWe have a winner!.\n")
                print("smoov moov " + move + " won.")
                break
            elif gameboard['4'] == gameboard['5'] == gameboard['6'] != ' ':  # this checks the board through the middle
                printBoard(gameboard)
                print("\nGame Over.\n")
                print("smoov moov " + move + " won.")
                break
            elif gameboard['1'] == gameboard['2'] == gameboard['3'] != ' ':  # this checks the board across the bottom
                printBoard(gameboard)
                print("\nGame Over.\n")
                print("smoov moov " + move + " won.")
                break
            elif gameboard['1'] == gameboard['4'] == gameboard['7'] != ' ':  # this checks the board down the left side
                printBoard(gameboard)
                print("\nGame Over.\n")
                print("smoov moov " + move + " won.")
                break
            elif gameboard['2'] == \
                    gameboard['5'] == gameboard['8'] != ' ':  # this checks the board down the middle
                printBoard(gameboard)
                print("\nGame Over.\n")
                print("smoov moov " + move + " won.")
                break
            elif gameboard['3'] == gameboard['6'] == gameboard['9'] != ' ':  # this checks the board down the right side
                printBoard(gameboard)
                print("\nGame Over.\n")
                print("smoov moov " + move + " won.")
                break
            elif gameboard['7'] == gameboard['5'] == gameboard['3'] != ' ':  # this checks the board down left diagonal
                printBoard(gameboard)
                print("\nGame Over.\n")
                print("smoov moov " + move + " won.")
                break
            elif gameboard['1'] == gameboard['5'] == gameboard['9'] != ' ':  # this checks the board up right diagonal
                printBoard(gameboard)
                print("\nGame Over.\n")
                print(" smoov moov " + move + " won.")
                break

                # In most cases Tic-Tac-Toe ends in a draw so we create an iif statement for that scenario
        if count == 9:
            print("\nSmooooov\n")
            print("You both win! Or lose, whichever you decide")

        # These next statements allow us to change turns, making sure nobody cheats.
        if move == 'X':
            move = 'O'
        else:
            move = 'X'

            # Since it was probably a tie, we will ask if they want to play again
def close_game():
    while True:
        reset = input("would you like to play again?(y/n)")
        if reset.lower().startswith("y"):
            for key in board_keys:
                gameboard[key] = " "

            game()
        elif reset.lower().startswith("n"):
            print("Thank you for playing my version of Tic-Tac-Toe, have a great day!")
            quit()
        else:
            print("sorry I did not understand your input")

game()
close_game()