def list_tuple(list_param: list, element: int):
    positions = []
    for i in range(len(list_param)):
        if list_param[i] == element:
            positions.append(i)
    tup_elements = tuple(positions)
    return tup_elements


def create_input_int_list(length: int):
    list = []
    for i in range(length):
        value = int(input("Enter value: "))
        list.append(value)
    return list


#create the list based on input
list_global_length = int(input("Enter lenght for the list: "))
list_global = create_input_int_list(list_global_length)
print("Created list is:",list_global)

#get the element
element_global = int(input("Enter the element: "))

#use functions
tup_elements_global = list_tuple(list_global,element_global)
print(tup_elements_global)


