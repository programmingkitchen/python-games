'''
    Rock Paper Sissors game
    This is the complete game with winner logic added.
'''

import random

# Global variables keep score and don't need to be passed into functions.
win = 0
loss = 0
tie = 0

def main():
    #control loop with 'y' variable
    play_again = 'y'

    #start the game
    while play_again == 'y':
        display()
        scoreboard()
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("RESULT: ", pick_winner(user_choice, computer_choice))
        print("User choice: ", user_choice)
        print("Computer choice: ", computer_choice)
        scoreboard()
        play_again = input("Play again? (y/n): ")

        if play_again != "y":
            print("\n\nThank you for playing.")
            print("FINAL SCORES.")
            print("Win:\t", win)
            print("Loss:\t", loss)
            print("Tie:\t", tie)


# Intial display
def display():
    print("\n\n========================================")
    print("Let's play Rock, Paper, Sissors!")

# Display the scores
def scoreboard():
    print("\nThe current scores.")
    print("Win:\t", win)
    print("Loss:\t", loss)
    print("Tie:\t", tie)

# Loop continues until a valid choice is entered or ^C
def get_user_choice():
    while True:
        user_choice = input("\nType one of the following: rock, paper, or sissors: ")
        if user_choice == "rock" or user_choice == "paper" or user_choice == "sissors":
            return user_choice
        else:
            print("ERROR:  Not a valid choice.")

# Get the computer choice
def get_computer_choice():
    computer_choice = ['rock', 'paper', 'sissors']
    return random.choice(computer_choice)

# TODO: add the logic for the winner
def pick_winner(user_choice, computer_choice):
    global win
    global loss
    global tie

    if computer_choice == user_choice:
        tie = tie + 1
        return "tie"

    if user_choice == 'rock':
        if computer_choice == 'paper':
            loss = loss + 1
        else:
            win = win + 1
    elif user_choice == 'paper':
        if computer_choice == 'sissors':
            loss = loss + 1
        else:
            win = win + 1

    elif user_choice == 'sissors':
        if computer_choice == 'rock':
            loss = loss + 1
        else:
            win = win + 1
    else:
        print("ERROR: Something went wrong, we should never get here.")

# Format for running a main method.
if __name__ == "__main__":
    main()
