import random

random_number = random.randrange(0,21)
#the users number is float even though the
# random number is into so that if the user mistypes
# with a coma there is no problem
user_number = float()
number_of_guesses = int(1)
print("Try to guess the number: ")

while user_number != random_number:
    user_number = float(input("Enter guess: "))
    if user_number > random_number:
        print("The number is smaller than", user_number)
    elif user_number < random_number:
        print("The number is greater than", user_number)
    else:
        print("Congratulations, you found the number!!")
    print("Number of tries:",number_of_guesses)
    number_of_guesses += 1

#Every 5 guesses the program asks you if you want to find out the number
    if number_of_guesses % 5 == 0:
        question = input("Want to find the answer? : Type Yes or No: ")
        if question == "Yes":
            print("The answer is",random_number)
        else:
            print("Keep guessing ")