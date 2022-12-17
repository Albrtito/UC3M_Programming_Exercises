import random


# turn string input values for ROCK PAPER SCISSORS into numerical values 0,1,2
def input_to_numerical(input__def):
    numerical_input = 0
    if input__def == "ROCK":
        numerical_input = 0
    elif input__def == "PAPER":
        numerical_input = 1
    elif input__def == "SCISSORS":
        numerical_input = 2

    return numerical_input


# Turn numerical values 0,1,2 into strings ROCK PAPER SCISSORS
def numerical_to_input(numerical):
    string_input = 0
    if numerical == 0:
        string_input = "ROCK"
    elif numerical == 1:
        string_input = "PAPER"
    elif numerical == 2:
        string_input = "SCISSORS"

    return string_input


# Possible move combinations in a table in order to check who won
moves = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]

# Constant for the number of games to play
number_of_games = 5
print("*****", number_of_games, "will be run")

# Run the code the times necessary, times given by the number of games constant
for number_of_games in range(number_of_games):
    # ask the player for an input
    print("ROCK, PAPER OR SCISSORS?")
    player_input = input()
    # create a random input for the computer from 0 to 2 in order to use the moves table
    computer_choice = random.randint(0, 2)
    # turn computer choice into a string with the method and print it
    print("Program chooses", numerical_to_input(computer_choice))
    # decide the winner move given the moves of the players and the winn moves table.
    # Whoever has the same value as the value in the table wins
    winner_move = moves[input_to_numerical(player_input)][computer_choice]
    # print the winner or the tie
    if computer_choice == winner_move:
        print("*****PROGRAM WINS*****")
    elif input_to_numerical(player_input) == winner_move:
        print("*****PLAYER WINS*****")
    else:
        print("*****TIE*****")
