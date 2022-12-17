# METHODS FOR LIST

def my_max(list: list):
    max_value = float(0)
    for i in range(len(list)):
        value = list[i]
        if value >= max_value:
            max_value = value
    return max_value


def my_min(list: list):
    min_value = list[0]
    for i in range(len(list)):
        value = list[i]
        if value < min_value:
            min_value = value
    return min_value


def my_average(list: list):
    sum_list = sum(list)
    average = sum_list / (len(list))
    return average


def create_input_int_list(length: int):
    list = []
    for i in range(length):
        value = int(input("Enter value: "))
        list.append(value)
    return list


# does not work for the for i in range?
def range_copy(stop: float or int, start=0, step=1):
    final_tup = ()
    final_list = []
    term = start
    final_list.append(term)
    if step < 0:
        while (term + step) >= stop:
            term = term + step
            final_list.append(term)
        final_tup = tuple(final_list)
    else:
        while (term + step) <= stop:
            term = term + step
            final_list.append(term)
        final_tup = tuple(final_list)
    return final_tup


def my_count(list1: list, x: int):
    count = 0
    for i in range(len(list1)):
        if list1[i] == x:
            count += 1
    return count


def my_index(list1: list, x: int):
    for i in range(len(list1)):
        if list1[i] == x:
            return i
    return None


def my_append(list1: list, x: int):
    list_copy = list1.copy()
    list_copy += [x]
    return list_copy


def my_insert(list1: list, x: int, index: int):
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


def my_remove(list1: list, x: int):
    list_copy = list1.copy()
    list_copy_1 = []
    for i in range(len(list_copy)):
        if list_copy[i] == x:
            for m in range(len(list_copy)):
                if (m < i) or (m > i):
                    list_copy_1 += [list_copy[m]]
            return list_copy_1

int = 1234
int_str = str(int)
print(len(int_str))