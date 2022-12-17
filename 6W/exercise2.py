import random
import create_list
list1 = []
list2 = []
create_list.create_int_list(list1)
list2 = list1
print(list2)
list1[1] = 2
print(list1)
print(list2)
"""
Giving a list the value of another one using the = operator 
creates a pointer to the same memory slot that the first list has.This 
means that any changes made to the first list will be made to the second one. 
They are the same list in memory and values
"""
