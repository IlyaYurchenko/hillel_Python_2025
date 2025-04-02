lst = []
lst_len = len(lst)

subdiv_lst = lst_len//2

if not lst_len:
    lst_new = [lst, lst]
    print(lst_new)

elif not lst_len % 2:
    lst_1 = lst[:subdiv_lst]
    lst_2 = lst[subdiv_lst:]
    lst_new = [lst_1, lst_2]
    print(lst_new)
else:
    lst_1 = lst[:subdiv_lst + 1]
    lst_2 = lst[subdiv_lst + 1:]
    lst_new = [lst_1, lst_2]
    print(lst_new)


