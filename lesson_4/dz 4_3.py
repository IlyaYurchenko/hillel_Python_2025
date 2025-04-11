import random
rand_len = random.randint(3,10)
lst = list(random.randint(0, 10) for i in range(rand_len))

print('start list: ', lst)

len_check = 0
new_lst = [lst[0], lst[2], lst[-2]]

print('new list: ',new_lst)