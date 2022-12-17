list = [2,3,34,5,6,7]
list[5] = list[3]
print(list[5])
print(list[3])
list[3] = 33
print(list[3])
print(list[5])
#value of list[3] is 33 and list[5] is stil 5
"""
Values of list [3] wont change when 
changing list[5] and values of list[5] 
wont change when changing list[3]. 
That copy only applies when assigning a list 
to another one such as list1 = list2
"""
