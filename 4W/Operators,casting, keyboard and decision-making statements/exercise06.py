# ask for user age
user_age = int(input("Input user age: "))


# define a function that returns a value of the price based on the age
def print_price(age):
    # declare a price variable based firstly on the normal ticket
    price = float(9)
    # price for age under 5
    if age < 5:
        price *= 0.6
    # price for age above 60
    if age > 60:
        price *= 0.55
    # price for ages between 5 and 26
    if 5 < age < 26:
        price *= 0.2
    return price


print(print_price(user_age))
