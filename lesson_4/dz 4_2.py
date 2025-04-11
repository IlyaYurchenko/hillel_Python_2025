lst = [0, 1, 7, 2, 4, 8]
len_check=len(lst)

if len_check > 0:
    new_lst = lst[:len_check:2]
    result = (sum(new_lst[:3])) * lst[-1]
    print('new list =', new_lst, 'new list sum =', sum(new_lst[:3]), 'list last element =', lst[-1],
          '\nresult =', result)
else:
    print(lst)


