var_1 = 1
var_2 = var_1
print(var_2)
var_1 += var_1
print(var_1)
print(var_2)
"""
The second one wont change its value because python runs lines one after the other, 
this means that the var_2 is assigned the value of variable 1 when var_1 is 1, so variable 
2 value is 1 and not var_1 with whatever changes var_1 could have. 
"""
