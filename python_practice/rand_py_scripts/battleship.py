"""
This program is intended to emulate the boardgame Battleship.
The user is given four opportunities to guess the locations of the ship(s),
after each attempt the program responds with a 'Hit' or 'Miss' message.
If after four attempts the user does not guess correctly the program outputs
a 'Loss' message and exits. 
Created on Tue Nov 15 19:33:10 2016

@author: Raymond P. McGuire
"""
#import randint
from random import randint
#create blank gameboard
board = []
while True:
#determine size of game board
    for x in range(5):
        board.append(["O"] * 5)
    #iterate through each row and print to user console in readable format
    def print_board(board):
        for row in board:
            print " ".join(row)
    #print welcome message and new gameboard to user console
    print "Let's play Battleship!"
    print_board(board)
    #randomly select row in which ship hides
    def random_row(board):
        return randint(0, len(board) - 1)
    #randomly select column in which ship hides
    def random_col(board):
        return randint(0, len(board[0]) - 1)
    #store row and column location in corresponding variables
    ship_row = random_row(board)
    ship_col = random_col(board)
    #begin user turns, acceot guesses
    for turn in range(4):
        print "Turn", turn + 1 #user first turn
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
    #evaluate user guess
        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!" #correct guess
            print_board(board) #print winning gameboard
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean." #guess out of bounds
            elif(board[guess_row][guess_col] == "X"): #identify user miss
                print "You guessed that one already." #guess is repeated
            else:
                print "You missed my battleship!" #incorrect guess
                board[guess_row][guess_col] = "X" #mark misses on gameboard
            print "Turn", turn + 1 #count subsequent turns
        if turn == 3:
            print "Game Over" # user failed to guess correctly in four turns
            board[ship_row][ship_col] = "S" #reveal ship location
            print_board(board) #print gameboard to user console
            while True:
                answer = raw_input('Run again? (y/n): ')
                if answer in ('y', 'n'):
                    break
                print 'Invalid input.'
            if answer == 'y':
                continue
            else:
                print 'Goodbye'
                break