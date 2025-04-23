def add_one(lst: list) -> list:
    new_lst = []
    lst_int = int(''.join(map(str, lst)))
    lst_int += 1

    for i in str(lst_int):
        new_lst.append(int(i))

    return new_lst

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")