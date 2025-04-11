lst = [1,2,3,4,5]
len_check=len(lst)
i= 0
new_lst = []

if len_check > 0:
    while i < len_check:
            if i == 0 or not i % 2:
                new_lst.append(lst[i])
            i += 1

    result = (sum(new_lst[:3])) * lst[-1]
    print('new list =', new_lst, 'new list sum =', sum(new_lst[:3]),
          'list last element =', lst[-1], '\nresult =', result)

else:
    print(lst)

