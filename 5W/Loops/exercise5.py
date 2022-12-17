import random


# Returns a new pin
def create_new_pin():
    pin = str()
    for letter in range(4):
        letter = str(random.randrange(0, 9))
        pin += letter

    print("Your pin is:", pin)
    return pin


# Returns a balance as a float
def create_new_balance():
    balance = float(random.uniform(50, 5000))
    print("Your balance is:", balance)
    return balance


# Returns a bool
def check_for_pin(pin_def):
    inserted_pin = (input("Enter pin: "))
    attempts = 3
    while attempts > 1:
        if inserted_pin == pin_def:
            return True

        else:
            attempts -= 1
            inserted_pin = (input("Enter pin: "))

    return False


# First operation
def deposit(balance_def):
    deposit = float(input("Quantity to deposit: "))
    balance_def += deposit
    print("The available balance in the account is:", balance_def)


# Second operation
def withdraw(balance_def):
    amount_to_withdraw = float(input("Choose the amount to withdraw: "))
    if amount_to_withdraw > balance_def:
        print("The withdrawal operation is denied")
    else:
        balance_def -= amount_to_withdraw
        print("The available balance in the account is:", balance_def)


# Third operation
def exit_atm(balance_def):
    print("The available balance in the account is:", balance_def)


# Use the defined functions

balance = create_new_balance()
pin = create_new_pin()

if check_for_pin(pin):
    print("""
    Welcome
    -----------------------
    1- Deposit
    2- Cash withdrawal
    3- Exit """)
    operation = int(input("Choose the operation, mark 1,2 or 3: "))
    if operation == 1:
        deposit(balance)
    if operation == 2:
        withdraw(balance)
    if operation == 3:
        exit_atm(balance)

else:
    print("Failed to enter account")
