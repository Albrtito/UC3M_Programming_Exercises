# Calculator
number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))
possible_operators = ["+", "-", "/", "*", "//", "**"]

print("These are the possible operators")
for i in possible_operators:
    print(i)

operator = input("Enter the desired operator: ")

if operator == "+":
    print(number_1 + number_2)
elif operator == "-":
    print(number_1 - number_2)
elif operator == "/":
    print(number_1 / number_2)
elif operator == "*":
    print(number_1 * number_2)
elif operator == "//":
    print(number_1 // number_2)
elif operator == "**":
    print(number_1 ** number_2)

else:
    print(number_1, operator, number_2)
