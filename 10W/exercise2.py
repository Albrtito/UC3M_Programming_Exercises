import random


def ask_for_number():
    number = int(input("Enter a number between 1 and 10: "))
    while number > 10 or number < 1:
        number = int(input("Enter a number between 1 and 10: y"))

    return number


def generate_list(number_of_elements: int):
    list = []
    for i in range(number_of_elements):
        list.append(random.randint(0, 1000))
    return list


def my_min(list: list):
    min_value = list[0]
    for i in range(len(list)):
        value = list[i]
        if value < min_value:
            min_value = value
    return min_value


input_number = ask_for_number()
list_global = generate_list(input_number)
min_value_list = my_min(list_global)

print(input_number, list_global, min_value_list)
