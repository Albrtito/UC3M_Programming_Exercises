def list_combination(list_1: list, list2: list):
    list_3 = list_1.copy
    for i in range(len(list2)):
        add = True
        for m in range(len(list_1)):
            if list2[i] == list_3[m]:
                add = False

        if add:
            list_3.append(list2[i])
    return list_3


list1 = [1, 1,  2, 3, 4, 5, 6]
list2 = [2, 5, 6, 7, 8, 9]
list3 = list_combination(list1,list2)
print("list1:",list1)
print("list2:",list2)
print("Output:",list3)
