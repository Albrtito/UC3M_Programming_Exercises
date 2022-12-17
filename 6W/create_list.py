import random

list = []
def create_int_list(list):
    for i in range(0, 20):
        list += [random.randint(0, 1000)]

    print(list)

