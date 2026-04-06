
#Displaying the dipict board structure. 
def display_board(B_board):# boarding display parameter 
    print("\n")
    print(f" {B_board[0]} | {B_board[1]} | {B_board[2]} ")
    print("---|---|---")
    print(f" {B_board[3]} | {B_board[4]} | {B_board[5]} ")
    print("---|---|---")
    print(f" {B_board[6]} | {B_board[7]} | {B_board[8]} ")
    print("\n")

# checking the 
def check_win(B_board, player):

# Multi_dimentional array(matrix) within a list.
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    for items in win_conditions:

    # comprehension list with "all" builtin function to check all the values in the board are non Zero(for int)/ false(fo bool)/Empty Space(for string).

        if all(B_board[i] == player for i in items): 
            return True
    return False



def check_draw(B_board):
    return all(cell != " " for cell in B_board) # checking weather X or O are drawn   


def player_move(B_board, player):
 # Use the Execptional hundling to checking the position availability and verifiying the movement. 
    while True:
        try:
            move = int(input(f"Player {player}, enter position (1-9): ")) - 1 # Index value->(User input value-1)

            if move < 0 or move > 8: # N.B 0 and 8 are indedx Values in the board 
                print("OOPS!!! Invalid position. Choose 1–9.")

            elif B_board[move] != " ":  
                print("OOPS!!! Spot already taken. Try again.")

            else:
                B_board[move] = player
                break

        except ValueError:
            print("OOPS!!! Please enter a valid number.")


def tic_tac_toe():
    B_board = [" "] * 9 # Create the empty bill board with 3 Row X 3 Coloumn. 
    current_player = "X" # The player who provide the current input.

    print(" Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1–9 like this:\n")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 \n")

    while True: # Keep repeating this block forever until I explicitly stop it.
        display_board(B_board)
        player_move(B_board, current_player)

        if check_win(B_board, current_player):
            display_board(B_board)
            print(f" Player {current_player} wins!")
            break

        if check_draw(B_board):
            display_board(B_board)
            print(" It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__": # The file is the main program.
    tic_tac_toe()
    
#########################################
# Author: Hunde Tolera                  #
# Date: 04/05/2026                      #
#########################################
    
