# Calculator
op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y,
      '//': lambda x, y: x // y,
      '**': lambda x, y: x ** y}

number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))
possible_operators = ["+", "-", "/", "*", "//", "**"]

print("These are the possible operators")
for i in possible_operators:
    print(i)

operator = input("Enter the desired operator: ")
"""
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
"""

for i in possible_operators:
    if operator == i:
        print(op[i](number_1, number_2))
