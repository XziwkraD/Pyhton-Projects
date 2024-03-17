def display_board(): #displays the board using nested loops
#print the top border of the board
    print("+-------+-------+-------+")

#iterate over each row in the board
    for row in board:
    #print the empty row on top of each cell
        print("|       |       |       |")
        #iterate over each number in the current row
        for num in row:
            print(f"|   {num}   ", end= "")
        #move on to the next line after printing all numbers in the row
        print("|")
        #print the bottom row of each cell
        print("|       |       |       |")
        #print the line seperating the rows as well as the bottom border of the board
        print("+-------+-------+-------+")

def board_update(move, symbol):
    #map the user's move to become board indices
    move = int(move)
    while True:
        row = (move - 1) // 3
        col = (move - 1) % 3

        #check if the selected cell is empty beffore updating
        if board[row][col] not in ["X", "O"]:
            #update the board
            board[row][col] = symbol
            display_board()
            return True
        else:
            print("Cell is already occupied, please re-enter your move(1-9).")
            move = int(input("Enter your move: "))

def board_update_com(move, symbol):
    #map the user's move to become board indices
    move = int(move)
    while True:
        row = (move - 1) // 3
        col = (move - 1) % 3

        #check if the selected cell is empty beffore updating
        if board[row][col] not in ["X", "O"]:
            #update the board
            board[row][col] = symbol
            display_board()
            return True
        return False

def is_winner(symbol): #symbol represents 'X' or 'O'
    #check rows for a winner
    for row in board:
        if all(num == symbol for num in row):# The all() function in Python is a built-in function that returns True if all elements in an iterable are True, and it returns False otherwise.
            return True                      # It's particularly useful when you want to check if all elements in a sequence meet a certain condition.
    #check columns for a winner
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)): # iterate over each column (basically vertically) and check if all the cells in that column have the same symbol,
            return True                                        # and you do this by varying the row index while keeping the column index constant,
    #check diagonals for a winner                              # so it'll iterate as such: [0][0], [1][0], [2][0], [0][1], [1][1], [2][1] etc.
    if all(board[i][i] == symbol or board[i][2-i] == symbol for i in range(3)):
        return True
    #no winners found
    return False

def is_board_full(): #checks if the board is full of symbols alr
    if all(isinstance(board[i][j], int) for i in range(3) for j in range(3)):
            return True
    return False

def is_game_over():
    if is_winner("X"):
        print("You Win!")
        return True
    elif is_winner("O"):
        print("The computer wins!")
        return True
    elif is_board_full() is True:
        print("The board has been filled!\nGAME OVER")
        return True
    else:
        return False

import random

def computer_move():
    #checks if the game is over before entering its move
    if is_game_over():
        return
    while True:
    #generates a random integer
        computer_choice = random.randint(1, 9)
        print(f"The computer chooses {computer_choice}")
        if board_update_com(computer_choice, "O"):
            break
        else:
            print("Cell is already occupied, choosing a new move.")



#Step 1: print out the empty board

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#Step 2: display the board using nested loops

display_board()

#Step 3: Prompt user to input their move (1 to 9)

while True: ####### Main game loop that continues till someone wins ######
    user_move = input("Enter your move: ")
    
    if not user_move.isdigit():
        print("You have not entered an integer, please re-enter your move(1-9).")
    elif int(user_move) > 9:
        print("You have entered too high a number, please re-enter your move(1-9).")
    elif int(user_move) < 1:
        print("You have entered too low a number, please re-enter your move(1-9).")

        #Step 4: update the board  
    else:
        board_update(user_move, "X")

    #Step 5: check to see if game has ended
    if is_game_over():
        break

    #Step 6: computer's move
    computer_move()

    if is_game_over():
        break