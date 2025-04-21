import random

def common_elements():
    lst_1 = [i for i in range(100) if i % 3 == 0]
    lst_2 = [j for j in range(100) if j % 5 == 0]
    intersection = set(lst_1).intersection(set(lst_2))

    return intersection

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
