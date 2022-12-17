import random

def generate_random_minmax (minimum: float, maximum:float, type_of_value: str):
    if type_of_value == "complex":
        number = complex(random.randint(minimum,maximum))
    if type_of_value == "float":
        number = random.uniform(minimum,maximum)
    if type_of_value == "int":
        number = random.randint(minimum,maximum)

    return number

minimum = float(input("Enter minimum: "))
maximum = float(input("Enter maximum: "))
value_type = input("Enter complex, float or int: ")
random_number = generate_random_minmax(minimum, maximum, value_type)
print(random_number)