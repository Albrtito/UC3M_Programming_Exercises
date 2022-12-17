import random
number_of_games = int(input("Enter number of games to play: "))

for i in range(number_of_games):
    turn_one = True
    turn_two = True
    can_win_1 = True
    can_win_2 = True
    points_1 = 0
    points_2 = 0
    print("START OF GAME",i+1)

    """
    Use a for loop instead of two whiles
    """
    while turn_one:
        print("GAME",i + 1," - PLAYER 1")
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        points_1 += dice_2 + dice_1
        print("The number of points obtained are", points_1)
        if points_1 > 21:
            turn_one = False
            turn_two = False
            can_win_1 = False
            print("Player one looses, points are", points_1)
        if points_1 == 21:
            turn_two = False
            turn_one = False
            print("*****PLAYER 2 WINS*****")

        else:
            hit = input("Enter HIT if you want to roll the dices again, or enter NO HIT : ")
            if hit == "NO HIT":
                turn_one = False

    while turn_two:
        print("GAME",i + 1," - PLAYER 2")
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        points_2 += dice_2 + dice_1
        print("The number of points obtained are", points_2)
        if points_2 > 21:
            turn_two = False
            can_win_2 = False
            print("Player two looses, points are", points_2)
        if points_2 == 21:
            turn_two = False
            print("*****PLAYER 2 WINS*****")

        else:
            hit = input("Enter HIT if you want to roll the dices again, or enter NO HIT: ")
            if hit == "NO HIT":
                turn_two = False

    if can_win_1 == True and can_win_2 == True:
        if (points_1 - points_2) > (points_2 - points_1):
            print("*****PLAYER 1 WINS*****")
        elif points_1 == points_2:
            print("*****TIE*****")
        else:
            print("*****PLAYER 2 WINS*****")