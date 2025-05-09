def binary_search(array, target):
    low, high = 0, len(array)-1

    while low <= high:
        mid = (low+high)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low =  mid + 1
        elif array[mid] > target:
            high = mid-1
    return -1

my_list = [11, 12, 22, 25, 34, 64, 90]
result = binary_search(my_list, 22)
print("Індекс шуканого елемента:", result)