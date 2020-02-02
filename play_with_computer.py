import os
import random
from play_together import check_win


def main():
    """ Main function
    """
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player_to_move = False
    result = 0
    difficulty = int(input("Enter a difficulty [1 - 4]\n>> "))
    while difficulty < 1 or difficulty > 4:
        difficulty = int(input("Enter a difficulty [1 - 4]\n>> "))
    if difficulty == 1:
        make_move = level_1
    elif difficulty == 2:
        make_move = level_2
    elif difficulty == 3:
        make_move = level_3
    else:
        make_move = level_4

    while not result:
        draw_a_board(board)
        player_to_move = not player_to_move
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
        if result == 1:
            draw_a_board(board)
            print("\nYou win!\n")
            break
        elif result == -1:
            draw_a_board(board)
            print("\nDraw!\n")
            break
        player_to_move = not player_to_move
        board = make_move(board)
        result = check_win('O', board)
    else:
        if result == 1:
            draw_a_board(board)
            print("\nYou lose!\n")
        elif result == -1:
            draw_a_board(board)
            print("\nDraw!\n")
        

def level_1(board):
    """ Difficulty: easy
        Random
    """
    possible_to_play = [i for i, x in enumerate(board) if x != 'X' and x != 'O']
    board[random.choice(possible_to_play)] = 'O'
    return board

def level_2(board):
    """ Difficulty: medium
        Win in 1 move if possible
        Protect from win in 1 move
    """
    for letter in 'O', 'X':
        if ((board[3] == letter and board[6] == letter) or (board[1] == letter and board[2] == letter) or (board[4] == letter and board[8] == letter)) and board[0] != 'O':
            board[0] = 'O'
        elif ((board[0] == letter and board[2] == letter) or (board[4] == letter and board[7] == letter)) and board[1] != 'O':
            board[1] = 'O'
        elif ((board[0] == letter and board[1] == letter) or (board[5] == letter and board[8] == letter) or (board[4] == letter and board[6] == letter)) and board[2] != 'O':
            board[2] = 'O'
        elif ((board[0] == letter and board[6] == letter) or (board[4] == letter and board[5] == letter)) and board[3] != 'O':
            board[3] = 'O'
        elif ((board[1] == letter and board[7] == letter) or (board[3] == letter and board[5] == letter) or (board[0] == letter and board[8] == letter) or (board[2] == letter and board[6] == letter)) and board[4] != 'O':
            board[4] = 'O'
        elif ((board[3] == letter and board[8] == letter) or (board[4] == letter and board[3] == letter)) and board[5] != 'O':
            board[5] = 'O'    
        elif ((board[0] == letter and board[3] == letter) or (board[2] == letter and board[5] == letter) or (board[7] == letter and board[8] == letter)) and board[6] != 'O':
            board[6] = 'O'
        elif ((board[6] == letter and board[8] == letter) or (board[1] == letter and board[4] == letter)) and board[7] != 'O':
            board[7] = 'O'
        elif ((board[6] == letter and board[7] == letter) or (board[0] == letter and board[4] == letter) or (board[2] == letter and board[5] == letter)) and board[8] != 'O':
            board[8] = 'O'
        else: continue
        break
    else:
        possible_to_play = [i for i, x in enumerate(board) if x != 'X' and x != 'O']
        board[random.choice(possible_to_play)] = 'O'
    return board


def level_3(board):
    """ Difficulty: hard
        Fixed enemy's pairs
        and build his own
    """
    # for letter in 'O', 'X':
    #     if ((board[3] == letter and board[6] == letter) or (board[1] == letter and board[2] == letter) or (board[4] == letter and board[8] == letter)) and board[0] != 'O':
    #         board[0] = 'O'
    #     elif ((board[0] == letter and board[2] == letter) or (board[4] == letter and board[7] == letter)) and board[1] != 'O':
    #         board[1] = 'O'
    #     elif ((board[0] == letter and board[1] == letter) or (board[5] == letter and board[8] == letter) or (board[4] == letter and board[6] == letter)) and board[2] != 'O':
    #         board[2] = 'O'
    #     elif ((board[0] == letter and board[6] == letter) or (board[4] == letter and board[5] == letter)) and board[3] != 'O':
    #         board[3] = 'O'
    #     elif ((board[1] == letter and board[7] == letter) or (board[3] == letter and board[5] == letter) or (board[0] == letter and board[8] == letter) or (board[2] == letter and board[6] == letter)) and board[4] != 'O':
    #         board[4] = 'O'
    #     elif ((board[3] == letter and board[8] == letter) or (board[4] == letter and board[3] == letter)) and board[5] != 'O':
    #         board[5] = 'O'    
    #     elif ((board[0] == letter and board[3] == letter) or (board[2] == letter and board[5] == letter) or (board[7] == letter and board[8] == letter)) and board[6] != 'O':
    #         board[6] = 'O'
    #     elif ((board[6] == letter and board[8] == letter) or (board[1] == letter and board[4] == letter)) and board[7] != 'O':
    #         board[7] = 'O'
    #     elif ((board[6] == letter and board[7] == letter) or (board[0] == letter and board[4] == letter) or (board[2] == letter and board[5] == letter)) and board[8] != 'O':
    #         board[8] = 'O'
    #     else: continue
    #     break
    # else:
    #     if 'O' in board:
    #         if board[4] == 'X':
    #             possible_to_play = [i for i, x in enumerate(board) if x != 'X' and x != 'O']
    #             for i in possible_to_play:
    #                 if i % 2 != 0:
    #                     board[i] = 'O'
    #                     break
    #             else: 
    #                 board[random.choice(possible_to_play)] = 'O'
    #         else:
    #             pass
    #     else:
    #         if board[4] == 'X':
    #             board[random.choice([0, 2, 6, 8])] = 'O'
    #         else:
    #             board[4] = 'O'

    return board

def level_4(board):
    """ Difficulty: impossible
        Play idealy
        You lose or draw
    """
    return board


def draw_a_board(board):
    """ Draw or update the board in terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')
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
