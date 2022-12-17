import math

is_digit = False
previous_letter = None
var_1 = input("Enter digit: ")
finished = False

for letter in var_1:
    while is_digit and finished == False:
        if letter.isdigit() or letter == "." and previous_letter != ".":
            is_digit = True
            previous_letter == letter
        else:
            is_digit = False


if is_digit:
    print("The square of the entered number is",float(var_1)**2)