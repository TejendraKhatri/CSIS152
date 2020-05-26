'''
This program is a simple version of the Battleship game.
'''
__author__ = "Tejendra Khatri"
__date__ = "2017-05-1"

import battle

import random

import turtle
window = turtle.Screen()

def reveal(board):
    "This function reveals the position of the ship in the board."
    new_list = []
    for row in board:
        position = ''
        for x in row:
            a = x.color()
            if a == ('blue','blue'):
                position = position + "0"
            else:
                position = position + "+"
        new_list.append(position)
    new_list.reverse()
    new_list = end = "\n".join(new_list)
    print(new_list)
        
def main():

    #prompt the user for board size
    board_size = int(window.textinput("Battleship","Enter the size of the playing board(maximum limit = 10):"))
    while board_size > 10:
        board_size = int(window.textinput("Battleship","Enter the size of the playing board(maximum limit = 10):"))

    #prompt the user for the length of the ship
    ship_length = int(window.textinput("Battleship","Enter the length of the ship(maximum limit = 10:"))
    while ship_length > board_size:
        ship_length = int(window.textinput("Battleship","Enter the length of the ship(maximum limit = 10):"))

    #make the board for the game
    beard = battle.makeBoard(board_size)
    
    #hide the ship within the board
    hide = battle.hideShip(beard,ship_length)
    reveal(beard)
    attempts = 0
    hits = 0
    while hits != ship_length:
        x,y = window.textinput("battleship","Enter x and y coordinates separated by a comma:").split(",")
        check = battle.checkShot(beard,int(x),int(y))
        if check == True:
            hits = hits + 1
        attempts = attempts + 1
    print("Congratulations !!! You completed the game in",attempts,"attempts.")
    

    #clear the screen for a new game
    turtle.clearscreen()

    #prompt the user if he wants to play again
    again = window.textinput("Battleship","Enter Y to play again or any key to exit:")
    if again.upper() == "Y":
        battle.clear(beard)
        main()
    else: 
        print("Thank You for playing.")
    

if __name__ == "__main__":
    main()

