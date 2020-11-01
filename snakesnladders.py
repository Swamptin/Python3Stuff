#!/bin/python3
# Attempt to create a game of snakes and ladders through the command line
import sys
import random

theBoard = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ',
        '9':' ','10':' ','11':' ','12':' ','13':' ','14':' ','15':' ','16':' ',
        '17':' ','18':' ','19':' ','20':' ','21':' ','22':' ','23':' ','24':' ',
        '25':' ','26':' ','27':' ','28':' ','29':' ','30':' ','31':' ','32':' ',
        '33':' ','34':' ','35':' ','36':' ','37':' ','38':' ','39':' ','40':' '}

def rolldice():
    num=random.randint(1,6)
    return num

def move(pos,dice):
    newpos= int(pos)+dice
    theBoard[str(newpos)]='@'
    if theBoard[pos]=='@':
        theBoard[pos]=' '
    else:
        loc=theBoard[pos]
        loc=str.replace('@', '', 1)
        theBoard[pos]=loc

def checkwin():
    #TODO: Make this more generic
    lastSquare='40'
    if theBoard[lastSquare] == '@':
        print("You won the game!\n")

def printBoard():
    x = 3
    while x >= 0:
        if x % 2 == 0:
            if x == 0:
                print(theBoard[str(x*10)] + "|" + theBoard[str((x*10)-1)] + "|" + theBoard[str((x*10)-2)] + "|" + theBoard[str((x*10)-3)] + "|" + theBoard[str((x*10)-4)] + "|" + theBoard[str((x*10)-5)]) + "|" + theBoard[str((x*10)-6)] + "|" + theBoard[str((x*10)-7)] + "|" + theBoard[str((x*10)-8)] + "|" + theBoard[str((x*10)-9)])
            else:
                print(theBoard[str(x*10)] + "|" + theBoard[str((x*10)-1)] + "|" + theBoard[str((x*10)-2)] + "|" + theBoard[str((x*10)-3)] + "|" + theBoard[str((x*10)-4)] + "|" + theBoard[str((x*10)-5)] + "|" + theBoard[str((x*10)-6)] + "|" + theBoard[str((x*10)-7)] + "|" + theBoard[str((x*10)-8)] + "|" + theBoard[str((x*10)-9)])
                print("-+-+-+-+-+-+-+-+-+-+-")
        elif x % 2 == 1:
            print(theBoard[str((x*10)+9)] + "|" + theBoard[str((x*10)+8)] + "|" + theBoard[str((x*10)+7)] + "|" + theBoard[str((x*10)+6) + "|" + theBoard[str((x*10)+5)] + "|" + theBoard[str((x*10)+4)] + "|" + theBoard[str((x*10)+3)] + "|" + theBoard[str((x*10)+2)] + "|" + theBoard[str((x*10)+1)])
            print("-+-+-+-+-+-+-+-+-+-+-")
        x -= 1
            

if __name__ == "__main__":
    printBoard()
