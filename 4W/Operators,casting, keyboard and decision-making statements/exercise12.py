money_amount = float(input("Enter money amount: "))
notes = [500, 200, 100, 50, 20, 10, 5]
coins = [2, 1, 0.5, 0.20, 0.10, 0.05, 0.02, 0.01]

for i in notes:
    notes_needed = money_amount // i
    print(i, "$: ", notes_needed)
    money_amount %= i
    i += 1

#print(money_amount)

for i in coins:
    coins_needed = money_amount // i
    print(i, "$", coins_needed)
    money_amount %= i
    i += 1
