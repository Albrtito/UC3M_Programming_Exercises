name = 'Johnny Depp'
age = 55
height = 1.78
weight = 65.4
eyes = 'brown'
hair = 'brown'

print("Example")
print("Let’s talk about %s." %name)
print("He's %i years old" %age)
print("He’s %.6f meters tall." %height)
print("He’s %.8f kilograms heavy." %weight)
print("Actually that’s not too heavy.")
print("He has %s eyes and %s hair." % (eyes, hair))

print("Exercise")
print("Let’s talk about ", name)
print("He's", age, "years old")
print("He’s", height, "meters tall." )
print("He’s", weight, "kilograms heavy.")
print("Actually that’s not too heavy.")
print("He has", eyes, "eyes and", hair, "hair.")

"""
The difference is on the float decimal spaces, when introducing the value as in the 
example there are as many decimal spaces in the floats as the ones you specify.
However, by using the second method the there will be as many decimal points as 
defined in the variable declaration.
"""