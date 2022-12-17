import random

def my_max(list):
    max_value = float(0)
    for i in range(len(list)):
        value = list[i]
        if value >= max_value:
            max_value = value
    return max_value

def my_min(list):
    min_value = list[0]
    for i in range(len(list)):
        value = list[i]
        if value < min_value:
            min_value = value
    return min_value

def my_average(list):
    sum_list = sum(list)
    average = sum_list/(len(list))
    return average

def createListNumbers():
    list = []
    for i in range(10):
        # We are taking numbers from 0 to a thousand for this function
        number = random.randint(0,1000)
        while number % 2 != 0:
            number = random.randint(0,1000)
        list.append(number)
    return list

def calculate_figures(list : list):
    figures = []
    figures.append(my_min(list))
    figures.append(my_max(list))
    figures.append(my_average(list))
    return figures


new_list = createListNumbers()
print("The list created with the first function is: ",new_list)
calculated_figures = calculate_figures(new_list)
print("The min value of the list is: ",calculated_figures[0])
print("The max value of the list is: ",calculated_figures[1])
print("The average value of the list is: ",calculated_figures[2])
