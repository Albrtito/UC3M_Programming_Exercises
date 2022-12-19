import random

"""
Alberto Pascau Sáez
Create a program with a float list generator and other features
Create a program that allows the user to work with lists of float numbers.
The program will offer the user the following options:
1) Fill randomly a list where the user selects the number of elements and the upper and lower bound.
2) Fill randomly a list where the number of elements and the upper and lower bound are in the range [1,1000).
3) Manually enter a list: the user will select the number of elements and he/she will enter their values.
4) Shrink the list: the program will create a new list with half the size of the original list and that will
be the result of adding the elements of the original list by pairs (the first element of the resulting list will
be the result of adding the first and second elements of the original list, the second element will be the sum
of the third and the fourth, and so on). Consider the case where the original list has an odd number of elements.
5) Invert the list (without using the reverse method): once the list has been introduced, the program will
return a list where the elements are placed in reverse order (the first will be the last and so on)
6) Print a list: the program will print the list, truncating the numbers to their integer values."""


# Functions that will be used

# This function is used for both the pseudo and random creation of list. It makes changes on the list given
def pseudo_random(list_created: list,
                  number_of_elements: int = random.randint(1, 9999), upper_bound: int = random.randint(1, 9999),
                  lower_bound: int = random.randint(1, 9999), ):
    # This line is only executed when the function is being used for random mode. The change happens outside
    if lower_bound > upper_bound:
        lower_bound = random.randint(1, upper_bound)
    """This function takes a number of elements,upper bound and lower bound and creates a pseudo random list with 
    them """
    for i in range(number_of_elements):
        new_element = random.randint(lower_bound, upper_bound)
        list_created.append(new_element)


# This function makes changes on the list given
def manual_list(list_created: list, number_of_elements: int):
    """This function creates a list based on values given by the user"""
    for i in range(number_of_elements):
        new_element = int(input(f"Enter element {i}: "))
        list_created.append(new_element)


# This function returns a list
def shrink_list(list_created: list):
    """This function returns a list with the sum of every two terms of another list given as a parameter"""
    new_list = []
    # If the element index is even, we get the next element, sum them up and add them to the new list
    # Problem: If we have an odd number of elements the last one will give an error: Solution: Make it so if the number
    # of elements its odd, the range will be repeated one less

    # The len is even
    if len(list_created) % 2 == 0:
        for i in range(len(list_created)):
            if i % 2 == 0:
                new_list.append(list_created[i] + list_created[i + 1])
    # The len is odd
    else:
        for i in range(len(list_created) - 1):
            if i % 2 == 0:
                new_list.append(list_created[i] + list_created[i + 1])
        # We add the last element that we did not add in the for loop
        new_list.append(list_created[len(list_created) - 1])
    return new_list


# This function returns a list
def reverse_list(list_created: list):
    new_list = []
    # We go through the list backwards. We start at the len, we stop at 0 and we step -1 each time
    for i in range(len(list_created) - 1, -1, -1):
        new_list.append(list_created[i])
    return new_list


"""
Two states in the game. Initial and editing the list. Both represented with a bool variable. 
The initial state is when the user is creating the list that is going to be edited, at the final step of this state the 
variable is turned to false and every change is made in order to change state to editing.
"""
# We start in the initial state
initial = True
editing = False
# The variable list_created is the list that will be created
list_created = []
list_edit = []
# Choosing the list:

while initial:
    print("""
    How do you want to fill the list? 
    1) Partially random 
    2) Totally random
    3) Manually""")
    option = int(input("Enter selection: "))
    # If it is a correct input, we enter the choosing state, where we`ll create a list. Initial is set to false and
    # choosing is set to true
    if option == 1:
        # Create a partially random list
        # 1) Ask the user for the number of elements. Upper and lower bounds.
        number_of_elements = int(input("Enter the number of elements for the list: "))
        upper_bound = int(input("Enter the upper bound for the list: "))
        lower_bound = int(input("Enter the lower bound for the list: "))
        while lower_bound > upper_bound:
            lower_bound = int(input("Enter the lower bound for the list, must be lower than the upper bound:  "))
        pseudo_random(list_created, number_of_elements, upper_bound, lower_bound)
        # Once we enter in one of the options. We are no longer in the initial, but we are editing:
        initial = False
        editing = True
        list_edit = list_created.copy()
    elif option == 2:
        # Create a Totally random list
        pseudo_random(list_created)
        # Once we enter in one of the options. We are no longer in the initial, but we are editing:
        initial = False
        editing = True
        list_edit = list_created.copy()
    elif option == 3:
        # Create a list manually
        # Ask the user for the number of elements
        number_of_elements = int(input("Enter the number of elements for the list: "))
        manual_list(list_created, number_of_elements)
        # Once we enter in one of the options. We are no longer in the initial, but we are editing: We also create a
        # copy of the list we just obtained to be used in the editing process, saving the initial list.
        initial = False
        editing = True
        list_edit = list_created.copy()
    else:
        print("Value is not correct. Input 1,2 or 3")

"""Once we have created a list depending on what the user wants, we can start with the edit state."""
while editing:
    # PRINTING THE EDITING MENU
    # Print the list that is generated and the options to do something with it
    print(f"""The generated list is {list_edit}
        Enter the option
        A) Shrink the list
        B) Invert the list
        C) Quit""")

    # INPUT
    # We use the same variable as before not to create another one, as that variable is no longer in use
    option = input("Enter selection ( A, B ,C): ")

    # We check if the value that we inputed is correct: If it is not, we can`t go through to the options:
    while option != "A" and option != "B" and option != "C":
        option = input("Enter the right value (A, B or C): ")

    # DECISION-MAKING BASED ON THE INPUT

    # If A is pressed we shrink the list
    if option == "A":
        list_edit = shrink_list(list_edit)

    # If B is pressed the list is reversed:
    if option == "B":
        list_edit = reverse_list(list_edit)
    # End the editing state if C is pressed.
    if option == "C":
        print("Thanks for using the list manager")
        editing = False
