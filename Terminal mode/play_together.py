import os


def main():
    """ Main function
    """
    player1_to_move = False
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 0
    while not result:
        player1_to_move = not player1_to_move
        draw_a_board(player1_to_move, board)
        print("Player 1 (X)" if player1_to_move else "Player 2 (O)", "to move:\n>> ", end="")
        try:
            move = int(input()) - 1
        except ValueError:
            move = -1
        while move < 0 or move > 8 or board[move] == 'X' or board[move] == 'O':
            draw_a_board(player1_to_move, board)
            print("Player 1 (X)" if player1_to_move else "Player 2 (O)", "to move\n", end="")
            try:
                move = int(input("\nERROR: Input an empty and possible to play number:\n>> ")) - 1
            except ValueError:
                move = -1
        board[move] = 'X' if player1_to_move else 'O'
        result = check_win('X' if player1_to_move else 'O', board)
    draw_a_board(player1_to_move, board)
    if result == 1:
        print("\nPlayer 1 (X)" if player1_to_move else "\nPlayer 2 (O)", "wins!\n")
    else:
        print("\nDraw!\n")


def draw_a_board(player1_to_move, board):
    """ Draw or update a board in a terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n---------Tic Tac Toe Game---------\n\n")
    print("Player 1 (X)    vs    Player 2 (O)\n\n")
    print("     |     |     ")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
    print("     |     |     \n")


def check_win(letter, board):
    """ Returns 1 if last player to move won
        Returns 0 if game continius
        Returns -1 if draw
    """
    if board[0] == letter and board[1] == letter and board[2] == letter or \
       board[0] == letter and board[4] == letter and board[8] == letter or \
       board[0] == letter and board[3] == letter and board[6] == letter or \
       board[1] == letter and board[4] == letter and board[7] == letter or \
       board[2] == letter and board[5] == letter and board[8] == letter or \
       board[3] == letter and board[4] == letter and board[5] == letter or \
       board[4] == letter and board[2] == letter and board[6] == letter or \
       board[6] == letter and board[7] == letter and board[8] == letter:
            return 1
    if board[0] == 1 or board[1] == 2 or board[2] == 3 or \
       board[3] == 4 or board[4] == 5 or board[5] == 6 or \
       board[6] == 7 or board[7] == 8 or board[8] == 9:
            return 0
    return -1


if __name__ == "__main__":
    main()