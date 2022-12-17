# this function return a tuple with the positions of a given element inside a list.
def get_positions_of_element(list_param: list, element: int):
    positions = []
    for i in range(len(list_param)):
        if list_param[i] == element:
            positions.append(i)
    tup_elements = tuple(positions)
    return tup_elements


# works
def my_count(list1: list, x: int):
    if type(list1) != list:
        raise TypeError
    if type(x) != int:
        raise TypeError
    count = 0
    for i in range(len(list1)):
        if list1[i] == x:
            count += 1
    return count


# works
def my_index(list1: list, x: int):
    if type(list1) != list:
        raise TypeError
    if type(x) != int:
        raise TypeError
    for i in range(len(list1)):
        if list1[i] == x:
            return i
    return None


# works
def my_append(list1: list, x: int):
    if type(list1) != list:
        raise TypeError
    if type(x) != int:
        raise TypeError
    list_copy = list1.copy()
    list_copy += [x]
    return list_copy


# works
def my_insert(list1: list, x: int, index: int):
    # check all parameters are of the right type
    if type(list1) != list:
        raise TypeError
    if type(x) != int:
        raise TypeError
    if type(index) != int:
        raise TypeError
    list_copy = list1.copy()
    list_copy_1 = []
    list_copy_2 = []
    # divide the list in two, add the element in the first half, add the second
    # half
    for i in range(len(list_copy)):
        if i < index:
            list_copy_1 += [list_copy[i]]
        elif i >= index:
            list_copy_2 = my_append(list_copy_2, list_copy[i])

    final_list = list_copy_1 + [x] + list_copy_2
    return final_list


# works
def my_remove(list1: list, x: int):
    # check all parameters are of the right type
    if type(list1) != list:
        raise TypeError
    if type(x) != int:
        raise TypeError

    list_copy = list1.copy()
    list_copy_1 = []
    for i in range(len(list_copy)):
        if list_copy[i] == x:
            for m in range(len(list_copy)):
                if (m < i) or (m > i):
                    list_copy_1 += [list_copy[m]]
            return list_copy_1


# does not work -> creating two or more list each one without one of the elements of the type
# to remove: Ex -> (1,2,3,4,5,6,7,2) -> (1,3,4,5,6,7,2) + (1,2,3,4,5,6,7)
def my_remove_all(list1: list, x: int):
    # check all parameters are of the right type
    if type(list1) != list:
        raise TypeError("The parameter list1 must be a list")
    if type(x) != int:
        raise TypeError

    list_copy = list1.copy()
    positions_of_x = get_positions_of_element(list_copy, x)
    for i in range(len(list_copy) - len(positions_of_x) + 1):
        list_copy_1 = []
        if list_copy[i] == x:
            for m in range(len(list_copy)):
                if (m < i) or (m > i):
                    list_copy_1 += [list_copy[m]]
            list_copy = list_copy_1.copy()

    return list_copy_1


# remove all elements of the list -> this will be done by creating a new empty list and returning that list
def my_clear(list1: list):
    # check all parameters are of the right type
    if type(list1) != list:
        raise TypeError

    # create and return the new list
    list_final = []
    return list_final


# pop must remove the last element of the list and return its value
"""
We`ll be copying all elements of a list except the last one to another one
"""


def my_pop(list1: list):
    # first copy the list into a new one so we are not changing the list given
    # check all parameters are of the right type
    if type(list1) != list:
        raise TypeError
    list2 = []
    last_element = list1[len(list1)-1]
    for i in range(1, len(list1) - 1):
        list2 += [list1[i]]
    return last_element


list_global = [1, 2, 3, 4, 5, 2, 6, 7, 2]
element = 2
print("Count:", my_count(list_global, element))
print("Index:", my_index(list_global, element))
print("Append:", my_append(list_global, element))
print("Insert:", my_insert(list_global, element, 3))
print("Remove:", my_remove(list_global, element))
print("RemoveAll:", my_remove_all(list_global, element))
print("Clear:", my_clear(list_global))
print("Pop:", my_pop(list_global))
print(list_global)
