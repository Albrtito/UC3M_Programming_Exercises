
var_1 = (input("Any character: Only single characters: "))

if len(var_1) != 1:
    print("Wrong variable length")

if var_1.isnumeric():
    print("It`s a number")
else:
    print("It`s not a number")


