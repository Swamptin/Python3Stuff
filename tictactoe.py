#!/bin/python3
import sys

theBoard = {'7':' ' , '8':' ' , '9':' ' ,
            '4':' ' , '5':' ' , '6':' ' ,
            '1':' ' , '2':' ' , '3':' ' }

board_keys = []

def printBoard(board):
    j=7
    i=0
    while i < 3:
        print(board[str(j-(i*3))] + '|' + board[str(j-(i*3)+1)] + '|' + board[str(j-(i*3)+2)])
        if i<2:
            print('-+-+-')
        i+=1

def checkWin(startPoint):
    i=0
    while i < 3:
        if theBoard[str(startPoint-(i*3))] == theBoard[str(startPoint-(i*3)+1)] == theBoard[str(startPoint-(i*3)+2)] != ' ':
            return True
        if theBoard[str(startPoint+i)] == theBoard[str((startPoint+i)-3)] == theBoard[str((startPoint+i)-6)] != ' ':
            return True
        i += 1
    if theBoard[str(startPoint)] == theBoard[str(startPoint-2)] == theBoard[str(startPoint-4)] != ' ':
        return True
    if theBoard[str(startPoint+2)] == theBoard[str(startPoint-2)] == theBoard[str(startPoint-6)] != ' ':
        return True


def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ". Move to which place?")

        move = input()

        if move.isdigit():
            if int(move)>9 or int(move)<1:
                print("That position doesn't exits.\nMove to which place?")
                continue
            elif theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue
        else:
            print("We only accept numbers.\nPlease enter a number between 1 and 9.")
            continue

        # Now we check if player X or player O has won, for every move after 5 moves
        if count >= 5:
            if checkWin(7):
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" *** " + turn + " won. *** ")
                break

        # If neither X nor O win:
        if count == 9:
             print("\nGame Over.\n")
             print("It's a tie!!\n")
             restart()

        # we change the player
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    for key in theBoard:
        board_keys.append(key)

    restart()

def restart():
    restart = input("Do you want to play again? (y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "
        game()
    else:
        sys.exit("Game no longer continued.")

if __name__ == "__main__":
    game()
