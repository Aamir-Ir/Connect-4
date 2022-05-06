# Name: Aamir Irfan, Tanuj Chada
# Date: January 7, 2019
# File Name: Connect4
# Description: This program is the base of a game called connect 4.
# Test cases: User input

# Importing modules needed for the game
import random
import time

# Intializing Variables
row1 = [0,0,0,0,0,0,0] # bottom row
row2 = [0,0,0,0,0,0,0]
row3 = [0,0,0,0,0,0,0]
row4 = [0,0,0,0,0,0,0]
row5 = [0,0,0,0,0,0,0]
row6 = [0,0,0,0,0,0,0]

rows = [row1, row2, row3, row4, row5, row6]

check = []

user = 1

def introduction():
    print("""Welcome to the game, you while be playing connect 4 just to inform you of the rules
        you have a game where you have to place pices inorder to connect 4 postions
        you can use complex strategies inorder to confuse your opponent.""")

class fullslot_error (Exception):
    pass
def haswon():
    print("Player " + str(user) + "has won")
    time.sleep(2)

def columns_and_rows():
    print("", row6, "\n", row5, "\n", row4,"\n", row3, "\n", row2, \
          "\n", row1)

def user_def():
    global user
    if user < 2:
        user = 2
    else:
        user = 1
    return user
    
def connect4():
    while True:
        try:
            if row6[user_input - 1] != 0:
                raise fullslot_error
            else:
                break
        except fullslot_error:
            print("Postion is full try again")
            confirm_def()

def confirm():
    looop = True
    while looop == True:
        try:
            global user_input
            user_input = int(input("input a position player " \
                + str(user) + "(1, 7) \n"))
            columns_and_rows()
            if user_input < 8 and user_input > 0:
                loop = False
            else:
                print("invalid int")
        except ValueError:
            print("Invalid Input")

def placement():
    counter = 0
    for i in range(0, 7):
        connect4()
        if (rows[i][user_input -1] == 0):
            rows [i][user_input - 1] = int(user)
            columns_and_rows()
            break

def check_def():
    global loop
    global check
    for i in range(0, 7):
        for a in range(0, 7):
            check.append(rows[i][a])
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            haswon()
            loop = False
            return loop
            break
        else:
            check = []
    for i in range(0, 7):
        for a in range(0, 7):
            check.append(rows[a][i])
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            haswon()
            loop = False
            return loop
            break
        else:
            check = []

def check_for_empty():
    global check
    for i in range(0, 7):
        for a in range(0, 7):
            check.append(grids[i][a])
    if 0 not in check:
        print("full")

def checks():
    check()
    check_for_empty()
    diagonalcheck()

def diagonal_check():
    global loop
    global check
    check = []
    diagonal = 0
    for i in range(0, 7):
        check.append(rows[diagonal][diagonal])
        diagonal = diagonal + 1
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            haswon()
            loop = False
            return loop
        break
    check = []
    diagonal = 3
    diagonal2 = 0
    for i in range(0, 7):
        check.append(rows[diagonal][diagnal2])
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            haswon()
            loop = False
            return loop
            break

loop = True

while loop == True:
    confirm()
    check_def()
    placement()
    checks()
    if loop == False:
        break
    user_def()
























                                   
