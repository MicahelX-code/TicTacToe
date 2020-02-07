import os
import play_together
import play_with_computer


while True:
    os.system('cls' if os.name == 'nt' else 'clear') # clears terminal
    print("\n---------Tic Tac Toe Game---------\n\n")
    if int(input("Enter number of players [1 to play against computer or 2 to play against someone nearby]:\n>> ")) == 1:
        play_with_computer.main() # runs play_with_computer.py
    else:
        play_together.main() # runs play_together.py
    if input("\nWant to play again? [Y/n]\n>> ").lower() == 'n':
        break
