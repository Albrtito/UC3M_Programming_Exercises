var_1 = 1e308 * 1e308
print(var_1)
#This will result in infinite
var_2 = 1e308 ** 1e308
print(var_2)


"""
This will result in an overflow error
unless one of the numbers is out
of range itself then it will compute
it as infinity and the result will
be infinity
"""

