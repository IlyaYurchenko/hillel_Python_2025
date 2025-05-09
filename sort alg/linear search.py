def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

my_list = [64, 34, 25, 12, 22, 11, 90]
result = linear_search(my_list, 22)
print("Індекс шуканого елемента:", result)