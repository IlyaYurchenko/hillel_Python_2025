lst = []
i = 0
len_check = 0
while len_check < len(lst):
    if lst[i] == 0:
        lst.append(lst.pop(i))
    else:
        i+=1
    len_check+=1

print(lst)
