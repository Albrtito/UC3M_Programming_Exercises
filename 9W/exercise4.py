def changeOfCurrency(original: str, target: str, quantity: float):
    currencies = (1.3, 4.5, 6.7, 5.4, 1) #based on the dollar
    """The dictionary takes the position in wich each currency is inside the tuple"""
    currencies_dictionary = {"dollar": 0, "yen": 1}
    """Get the value of each coin, original and target given their position in the dictionary
        Their position in dictionary is taken by the input the user gives"""
    original_position_value = currencies_dictionary.get(original)
    target_position_value = currencies_dictionary.get(target)
    """Get the exchange rate at wich each coin changes witht respect to the dollar"""
    exchange = currencies[target_position_value] / currencies[original_position_value]
    final_money = quantity * exchange
    return final_money


original_currency = input("Enter the original currency: ")
target_currency = input("Enter the target currency: ")
quantity_to_change = float(input("Enter the quantity to change as a float: "))
changed_money = changeOfCurrency(original_currency,target_currency,quantity_to_change)
print(changed_money)