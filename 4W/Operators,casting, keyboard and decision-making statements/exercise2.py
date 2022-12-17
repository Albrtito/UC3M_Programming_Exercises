a, b, c, d = 5, 3, 20, 20
c -= (a + 1) / b - 3 + a % b
d -= (a + 1) / (b + 3 - 4 * a) % b
print("c:", c)
print("d:", d)

#Checking for values
print((a + 1) / b - 3 + a % b)
print((a + 1) / (b + 3 - 4 * a) % b)

"""
The code described in the exercise defines 4 variables and then proceeds to subtract
operations of the first two variables to the last ones by using -= command. This means 
that any result the operations have will be subtracted to the variables c and d. 

The first operation: (a + 1) / b - 3 + a % b  result = 1
The second one: (a + 1) / (b + 3 - 4 * a) % b result = 2.5714285714285716

The values printed of c and d are the subtractions of c - 1 and d - 2.5714285714285716
"""
