import random

rand_len = random.randint(3,10)
lst = list(random.randint(0, 10) for i in range(rand_len))
i = 0
len_check = len(lst)
new_lst = []
print('start list: ', lst)

while i < len_check:
    if i == 0 or i == 2 or i == len_check-2:
        new_lst.append(lst[i])
    i+=1

print('new list: ',new_lst)