# Name: Aamir Irfan, Tanuj Chada
# Date: January 11, 2019
# File Name: Connect4
# Description: This program is the base of a game called connect 4.
# Test cases: User input

import time
import random

# Intializing Variables
row1 = [0,0,0,0] # bottom row
row2 = [0,0,0,0]
row3 = [0,0,0,0]
row4 = [0,0,0,0]


grids = [row1, row2, row3, row4]

# Will be used to collect integers to check for a winner.
check = []

# Will be used to switch between players
user = 1

# Will be used for random intros at the start of the game.
random_intro = random.randint(1, 3)

def introduction(random_intro):
    if random_intro == 1:
        print("""Welcome to the game, you will be playing Connect 4. Just to inform you of the rules
you have a game where you have to place pieces in order to connect 4 position,
you can use complex strategies in order to confuse your opponent.""")
        
    elif random_intro == 2:
        print("Welcome to the game where you win if you get four in a row!")
        
    else:
        print("Welcome to this amazing board game, connect 4, fight to be the first to get 4 in a row to win!")

class fullSlot_error (Exception):
    pass

def winner():
    print ("player " + str(user) + " has won")
     
def rows_board():
    print ("", row4, "\n", row3, "\n", row2, "\n", row1)

def next_player():
    global user
    if user < 2:
        user = 2
    else:
        user = 1
    return user

def slot_full():
   while True:
        try:
            if row4[user_input -1] != 0:
                raise fullSlot_error
            else:
                break
        except fullSlot_error:
            print ("slot is full try again")
            confirm_input()

def confirm_input():
    loop_input = True
    while loop_input == True:
        try:
            global user_input
            user_input = int(input("\ninput a slot player "+str(user)+"(1,5)\n"))
            if user_input < 5 and 0 < user_input:   
                loop_input = False
            else:
                print ("invalid int")
        except ValueError:
            print ("invalid input")

def placement():
    counter = 0
    for i in range (0,4):
        slot_full()
        if (grids[i][user_input -1] == 0):
            grids [i][user_input - 1] = int(user)
            rows_board()
            break


def vertical_horizontal_check():
    global loop
    global check
    for i in range(0,4):
        for a in range(0,4):
            check.append(grids[i][a])
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            winner()
            loop = False
            return loop
            break
        else:
            check = []
    for i in range(0,4):
        for a in range(0,4):
            check.append(grids[a][i])
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            winner()
            loop = False
            return loop
            break
        else:
            check = []

def check_empty():
    global check
    for i in range (0,4):
        for a in range (0,4):
            check.append(grids[i][a])
    if 0 not in check:
        print ("full")

def all_needed_checks():
    vertical_horizontal_check()
    check_empty()
    diagonal_check()

def diagonal_check():
    global loop
    global check
    check = []
    diagonal_connect = 0
    for i in range (0,4):
        check.append (grids[diagonal_connect][diagonal_connect])
        diagonal_connect = diagonal_connect + 1
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            winner()
            loop = False
            return loop
            break
    check = []
    diagonal_connect = 3
    diagonal_connect2 = 0
    for i in range (0,4):
        check.append (grids[diagonal_connect][diagonal_connect2])
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            winner()
            loop = False
            return loop
            break

# Main Program

loop = True

introduction(random_intro)
time.sleep(5)
rows_board()
while loop != False:
    vertical_horizontal_check()
    confirm_input()
    placement()
    all_needed_checks()
    if loop == False:
        break
    next_player()
