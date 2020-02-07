import os
import random
from play_together import check_win


def main():
    """ Main function
    """
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9] # looks like a NumPad
    result = 0 # 0 while game is going
    difficulty = int(input("Enter a difficulty [1 - 3]\n>> "))
    # choose difficulty
    while difficulty < 1 or difficulty > 3:
        difficulty = int(input("Enter a difficulty [1 - 3]\n>> "))
    if difficulty == 1:
        make_move = level_1
    elif difficulty == 2:
        make_move = level_2
    else:
        make_move = level_3
    # main loop
    while not result:
        draw_a_board(board)
        try:
            players_move = int(input("Your turn:\n>> ")) - 1
        except ValueError:
            players_move = - 1
        while players_move < 0 or players_move > 8 or board[players_move] == 'X' or board[players_move] == 'O':
            draw_a_board(board)
            try:
                players_move = int(input("ERROR: Input an empty and possible to play number:\n>> ")) - 1
            except ValueError:
                players_move = -1
        board[players_move] = 'X'
        result = check_win('X', board)
        # win or draw (after player's move)
        if result == 1:
            draw_a_board(board)
            print("\nYou win!\n")
            break
        elif result == -1:
            draw_a_board(board)
            print("\nDraw!\n")
            break
        board = make_move(board)
        result = check_win('O', board)
    else:
        # lose or draw (after computer's move)
        if result == 1:
            draw_a_board(board)
            print("\nYou lose!\n")
        elif result == -1:
            draw_a_board(board)
            print("\nDraw!\n")


def level_1(board):
    """ Difficulty: easy

        Random possible to play square
    """
    possible_to_play = [i for i, x in enumerate(board) if x != 'X' and x != 'O']
    board[random.choice(possible_to_play)] = 'O'
    return board


def level_2(board):
    """ Difficulty: medium

        1) Win in 1 move if possible
        2) Protect from win in 1 move
        3) Or random possible to play square
    """
    # win in 1 or protect from win in 1
    for letter in 'O', 'X':
        if ((board[3] == letter and board[6] == letter) or (board[1] == letter and board[2] == letter) or (board[4] == letter and board[8] == letter)) and board[0] == 1:
            board[0] = 'O'
        elif ((board[0] == letter and board[2] == letter) or (board[4] == letter and board[7] == letter)) and board[1] == 2:
            board[1] = 'O'
        elif ((board[0] == letter and board[1] == letter) or (board[5] == letter and board[8] == letter) or (board[4] == letter and board[6] == letter)) and board[2] == 3:
            board[2] = 'O'
        elif ((board[0] == letter and board[6] == letter) or (board[4] == letter and board[5] == letter)) and board[3] == 4:
            board[3] = 'O'
        elif ((board[1] == letter and board[7] == letter) or (board[3] == letter and board[5] == letter) or (board[0] == letter and board[8] == letter) or (board[2] == letter and board[6] == letter)) and board[4] == 5:
            board[4] = 'O'
        elif ((board[2] == letter and board[8] == letter) or (board[4] == letter and board[3] == letter)) and board[5] != 'O' and board[5] == 6:
            board[5] = 'O'    
        elif ((board[0] == letter and board[3] == letter) or (board[2] == letter and board[4] == letter) or (board[7] == letter and board[8] == letter)) and board[6] == 7:
            board[6] = 'O'
        elif ((board[6] == letter and board[8] == letter) or (board[1] == letter and board[4] == letter)) and board[7] == 8:
            board[7] = 'O'
        elif ((board[6] == letter and board[7] == letter) or (board[0] == letter and board[4] == letter) or (board[2] == letter and board[5] == letter)) and board[8] == 9:
            board[8] = 'O'
        else:
            continue
        break
    else:
        possible_to_play = [i for i, x in enumerate(board) if x != 'X' and x != 'O']
        board[random.choice(possible_to_play)] = 'O'
    return board


def level_3(board):
    """ Difficulty: hard

        1) Win in 1 move if possible
        2) Protect from win in 1 move
        3) Build a pair and force player to block it   
    """
    # win in 1 or protect from win in 1
    for letter in 'O', 'X':
        if ((board[3] == letter and board[6] == letter) or (board[1] == letter and board[2] == letter) or (board[4] == letter and board[8] == letter)) and board[0] == 1:
            board[0] = 'O'
        elif ((board[0] == letter and board[2] == letter) or (board[4] == letter and board[7] == letter)) and board[1] == 2:
            board[1] = 'O'
        elif ((board[0] == letter and board[1] == letter) or (board[5] == letter and board[8] == letter) or (board[4] == letter and board[6] == letter)) and board[2] == 3:
            board[2] = 'O'
        elif ((board[0] == letter and board[6] == letter) or (board[4] == letter and board[5] == letter)) and board[3] == 4:
            board[3] = 'O'
        elif ((board[1] == letter and board[7] == letter) or (board[3] == letter and board[5] == letter) or (board[0] == letter and board[8] == letter) or (board[2] == letter and board[6] == letter)) and board[4] == 5:
            board[4] = 'O'
        elif ((board[2] == letter and board[8] == letter) or (board[4] == letter and board[3] == letter)) and board[5] != 'O' and board[5] == 6:
            board[5] = 'O'    
        elif ((board[0] == letter and board[3] == letter) or (board[2] == letter and board[4] == letter) or (board[7] == letter and board[8] == letter)) and board[6] == 7:
            board[6] = 'O'
        elif ((board[6] == letter and board[8] == letter) or (board[1] == letter and board[4] == letter)) and board[7] == 8:
            board[7] = 'O'
        elif ((board[6] == letter and board[7] == letter) or (board[0] == letter and board[4] == letter) or (board[2] == letter and board[5] == letter)) and board[8] == 9:
            board[8] = 'O'
        else:
            continue
        break
    else:
        if not 'O' in board: # first move
            if board[4] == 5:
                board[4] = 'O'
            else:
                possible_to_play = [i for i, x in enumerate(board) if x != 'X' and x != 'O' and \
                                    (x == 1 or x == 3 or x == 7 or x == 9)]
                board[random.choice(possible_to_play)] = 'O'
            return board
        else: # not a first move and there is no pairs
            if not 'X' in board[:3:] and 'O' in board[:3:]:
                    board[0 if board[0] == 1 else random.choice([1, 2])] = 'O'
            elif not 'X' in board[3:6:] and 'O' in board[3:6:]:
                    board[3 if board[3] == 4 else (1 if board[1] == 2 else 2)] = 'O'
            elif not 'X' in board[6:9:] and 'O' in board[6:9:]:
                    board[6 if board[6] == 7 else random.choice([7, 8])] = 'O'
            elif not 'X' in board[::3] and 'O' in board[::3]:
                    board[0 if board[0] == 1 else random.choice([3, 6])] = 'O'
            elif not 'X' in board[1::3] and 'O' in board[1::3]:
                    board[1 if board[1] == 2 else random.choice([4, 7])] = 'O'
            elif not 'X' in board[2::3] and 'O' in board[2::3]:
                    board[2 if board[2] == 3 else random.choice([5, 8])] = 'O'
            elif not 'X' in board[2:2:8] and 'O' in board[2:2:8]:
                    board[2 if board[2] == 3 else random.choice([4, 6])] = 'O'
            elif not 'X' in board[:4:] and 'O' in board[:4:]:
                    board[0 if board[0] == 1 else random.choice([4, 8])] = 'O'
            else:
                possible_to_play = [i for i, x in enumerate(board) if x != 'X' and x != 'O']
                board[random.choice(possible_to_play)] = 'O'
    return board


def draw_a_board(board):
    """ Draw or update the board in terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear') # clears terminal
    print("\n---------Tic Tac Toe Game---------\n\n")
    print("Player (X)     vs     Computer (O)\n\n")
    print("     |     |     ")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
    print("_____|_____|_____")       
    print("     |     |     ")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
    print("     |     |     \n")


if __name__ == "__main__":
    main()
