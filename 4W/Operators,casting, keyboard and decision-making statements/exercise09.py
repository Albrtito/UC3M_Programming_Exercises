coordinate_x = int(input("Enter x coordinate: "))
coordinate_y = int(input("Enter y coordinate: "))

# The int property is checked in the declaration of variables.
# We check for the variables not to be 0
if coordinate_x != 0 and coordinate_y != 0:
    # We check for the 4 possible possibilities of values in the 4 cuadrants
    if coordinate_x > 0 and coordinate_y > 0:
        print("1st")
    elif coordinate_x < 0 and coordinate_y < 0:
        print("3st")
    elif coordinate_x < 0 and coordinate_y > 0:
        print("2st")
    elif coordinate_x > 0 and coordinate_y < 0:
        print("4st")

else:
    print("The values are not valid")
