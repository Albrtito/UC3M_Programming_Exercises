
#first float variable
var_1 = float(12345678901234567.0)
#secod float variable
var_2 = float(12345678901234568.0)
#print the substraction of the two variables
print(var_1 - var_2)
#The result is 0.0, expressed as a float


#first int variable
var_3 = int(12345678901234567.0)
#secod int variable
var_4 = int(12345678901234568.0)
#print the substraction of the two variables
print(var_3 - var_4)
#The result is 0 expressed as a int, with no coma

"""
The difference between both operations is that in the int variables the variable
is stored without the decimal places and the operation is done with two integers.However 
in the float type operations, the zero behind the coma is expressed because the 
float variables store the decimal points and operate with them
"""

print(0.3 - 0.2)
"""""
In this operation the result will be 0.0999999999...8 instead of 0.1. This is because 
of the precision of the programming language. Python operates in binaries and we are 
asking to convert binaries to decimal, there is a 0.0000000...1 precision error in the 
conversion
"""

