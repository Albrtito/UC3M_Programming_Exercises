def perfect_number(number):
    # find all divisors of the number smaller than the number itself
    divisors = []
    #sum_of_divisors = int()
    i = number - 1
    while i != 0:
        if number % i == 0:
            divisors += [i]
        i -= 1

    if sum(divisors) == number:
        return True


input_number = float(input("Enter a number as the top limit to generate perfect numbers: "))

if input_number == 0:
    print("There are no perfect numbers")

while input_number != 0:
    if perfect_number(input_number):
        print("The number", input_number, "is perfect")
    input_number -= 1
